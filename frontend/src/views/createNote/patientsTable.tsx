import React, { useState } from "react";
import styles from "./index.module.scss";
import {
  Autocomplete,
  Button,
  Checkbox,
  FormControl,
  FormControlLabel,
  InputLabel,
  MenuItem,
  OutlinedInput,
  Select,
  TextField,
} from "@mui/material";
import { DesktopDatePicker, TimePicker } from "@mui/x-date-pickers";
import CurrencyInput from "react-currency-input-field";
import { FlexSpaceBetween } from "../../themes/customItems";
import { ReactComponent as CloseCircle } from "../../assets/img/close-circle.svg";
import { ReactComponent as AddCircle } from "../../assets/img/add-circle.svg";
import moment from "moment/moment";
import { IDateValue, IMedicalService } from "../../consts/types";
import { observer, useLocalObservable } from "mobx-react-lite";
import { DoctorStateKeeper } from "../../store";

const PatientsTable = observer(
  ({
    discount,
    setFormData,
    formData,
    setDiscount,
    dateValue,
    setDateValue,
    timeValue,
    timeChangeHandler,
    services,
    appointedServices,
    setAppointedServices,
  }: {
    discount: number;
    setFormData: any;
    formData: any;
    setDiscount: React.Dispatch<React.SetStateAction<number>>;
    dateValue: moment.Moment | null;
    setDateValue: React.Dispatch<React.SetStateAction<moment.Moment | null>>;
    timeValue: IDateValue;
    timeChangeHandler: (time, type) => void;
    services: IMedicalService[];
    appointedServices: {
      quantity: number;
      service: IMedicalService;
    }[];
    setAppointedServices: React.Dispatch<
      React.SetStateAction<
        {
          quantity: number;
          service: IMedicalService;
        }[]
      >
    >;
  }) => {
    //
    const doctorStateKeeper = useLocalObservable(
      () => DoctorStateKeeper.instance
    );
    const [serviceSearchText, setServiceSearchText] = useState<string>("");

    const handleChangeInput = (event) => {
      const { name, value } = event.target;
      if (name === "debt" || name === "price") {
        setFormData({
          ...formData,
          [name]: parseInt(value.match(/\d+/g).join("")),
        });
      } else {
        setFormData({ ...formData, [name]: value });
      }
    };

    return (
      <>
        <div className={styles.patients_main_table}>
          <div className={styles.left_table}>
            <div className={styles.table_title}>Детали</div>
            <div className={styles.table_wrapper}>
              <div className={styles.table_wrapper_block}>
                <div className={styles.table_row}>
                  <p className={styles.row_title}>Льгота</p>

                  <FormControl className={styles.table_dropdown}>
                    <InputLabel
                      id="demo-simple-select-label"
                      sx={[
                        {
                          top: "-12px",
                          fontSize: "14px",
                        },
                        {
                          "&.Mui-focused": {
                            top: 0,
                          },
                        },
                      ]}
                    >
                      Без скидок
                    </InputLabel>
                    <Select
                      labelId="demo-simple-select-label"
                      id="demo-simple-select"
                      value={discount}
                      label="Без скидок"
                      name="exemption"
                      onChange={(e) => {
                        setDiscount(e.target.value as number);
                        handleChangeInput(e);
                      }}
                      sx={{ height: "32px" }}
                    >
                      {Array(22)
                        .fill(1)
                        .map((_, index) => index * 5)
                        .map((discount, i) => (
                          <MenuItem key={i} value={discount}>
                            {discount}%
                          </MenuItem>
                        ))}
                    </Select>
                  </FormControl>
                </div>
              </div>

              <div className={styles.table_wrapper_block}>
                <div className={styles.table_row}>
                  <p
                    className={styles.row_title}
                    style={{ marginRight: "17px" }}
                  >
                    Дата приема
                  </p>

                  <DesktopDatePicker
                    label="Выберете дату"
                    inputFormat="DD/MM/YYYY"
                    className={styles.input_block}
                    value={dateValue}
                    onChange={setDateValue}
                    renderInput={(params) => (
                      <TextField
                        {...params}
                        sx={{ width: "270px", marginRight: "25px" }}
                      />
                    )}
                  />

                  <FormControlLabel
                    control={<Checkbox />}
                    label="Авто"
                    className={styles.checkbox_block}
                  />
                </div>

                <div className={styles.table_row}>
                  <p
                    className={styles.row_title}
                    style={{ marginRight: "10px" }}
                  >
                    Время начала
                  </p>

                  <TimePicker
                    label="Time"
                    value={timeValue.from}
                    className={styles.input_block}
                    onChange={(newValue) => timeChangeHandler(newValue, "from")}
                    renderInput={(params) => (
                      <TextField
                        {...params}
                        sx={{ width: "103px", marginRight: "15px" }}
                      />
                    )}
                  />

                  <p
                    className={styles.row_title}
                    style={{ marginRight: "10px" }}
                  >
                    Время завершения
                  </p>

                  <TimePicker
                    label="Time"
                    value={timeValue.to}
                    className={styles.input_block}
                    onChange={(newValue) => timeChangeHandler(newValue, "to")}
                    renderInput={(params) => (
                      <TextField {...params} sx={{ width: "103px" }} />
                    )}
                  />
                </div>
              </div>

              <div className={styles.table_wrapper_block}>
                <div className={styles.table_row}>
                  <p
                    className={styles.row_title}
                    style={{ marginRight: "30px" }}
                  >
                    Долг
                  </p>

                  <CurrencyInput
                    id="input-example"
                    name="debt"
                    onChange={handleChangeInput}
                    placeholder="Please enter a number"
                    value={appointedServices
                      .map(
                        (appointedService) =>
                          appointedService.service.cost *
                          appointedService.quantity *
                          (1 - discount / 100)
                      )
                      .reduce((prev, curr) => {
                        return prev + curr;
                      }, 0)
                      .toFixed(1)}
                    allowDecimals={true}
                    allowNegativeValue={false}
                    prefix="UZS "
                    className={styles.currency_input}
                    onValueChange={(value, name) => console.log(value, name)}
                  />
                </div>

                <div className={styles.table_row}>
                  <p
                    className={styles.row_title}
                    style={{ marginRight: "24px" }}
                  >
                    Итого
                  </p>

                  <CurrencyInput
                    id="input-example"
                    name="price"
                    placeholder="Please enter a number"
                    value={appointedServices
                      .map(
                        (appointedService) =>
                          appointedService.service.cost *
                          appointedService.quantity *
                          (1 - discount / 100)
                      )
                      .reduce((prev, curr) => {
                        return prev + curr;
                      }, 0)
                      .toFixed(1)}
                    allowDecimals={true}
                    allowNegativeValue={false}
                    onChange={handleChangeInput}
                    prefix="UZS "
                    className={styles.currency_input}
                    onValueChange={(value, name) => console.log(value, name)}
                    style={{ marginRight: "35px" }}
                  />

                  <FormControlLabel
                    control={<Checkbox />}
                    label="Вручную"
                    className={styles.checkbox_block}
                  />
                </div>
              </div>

              <div className={styles.table_row}>
                <p className={styles.row_title}>Направивший врач</p>

                <Autocomplete
                  disablePortal
                  sx={{ width: "282px" }}
                  value={formData.referring_doctor}
                  id="combo-box-demo"
                  onChange={(e, v) =>
                    setFormData({ ...formData, referring_doctor: v?.value })
                  }
                  options={[
                    {
                      label: "test3",
                      value: 1,
                    },
                    {
                      label: "test4",
                      value: 2,
                    },
                    {
                      label: "test5",
                      value: 3,
                    },
                  ]}
                  className={styles.input_block}
                  noOptionsText={"Направление не найдено"}
                  renderInput={(params) => (
                    <TextField
                      name="referring_doctor"
                      {...params}
                      label="Выберите направление"
                      InputLabelProps={{
                        sx: [
                          {
                            top: "-12px",
                            fontSize: "14px",
                          },
                          {
                            "&.Mui-focused": {
                              top: 0,
                            },
                          },
                        ],
                      }}
                    />
                  )}
                />
              </div>

              <div className={styles.table_row}>
                <p className={styles.row_title}>Источники информации</p>

                <Autocomplete
                  disablePortal
                  sx={{ width: "282px" }}
                  id="combo-box-demo"
                  value={formData.information_source}
                  onChange={(e, v) =>
                    setFormData({ ...formData, information_source: v?.value })
                  }
                  options={[
                    {
                      label: "1",
                      value: 1,
                    },
                    {
                      label: "2",
                      value: 2,
                    },
                    {
                      label: "3",
                      value: 3,
                    },
                  ]}
                  className={styles.input_block}
                  noOptionsText={"Источник не найдено"}
                  renderInput={(params) => (
                    <TextField
                      {...params}
                      label="Выберите источники"
                      name="information_source"
                      InputLabelProps={{
                        sx: [
                          {
                            top: "-12px",
                            fontSize: "14px",
                          },
                          {
                            "&.Mui-focused": {
                              top: 0,
                            },
                          },
                        ],
                      }}
                    />
                  )}
                />
              </div>

              <div className={styles.table_row}>
                <p className={styles.row_title}>Коммент нап врача</p>

                <OutlinedInput
                  onChange={handleChangeInput}
                  name="referring_doc_notes"
                  value={formData.referring_doc_notes}
                  className={styles.input_block}
                  sx={{ width: "282px" }}
                />
              </div>

              <div className={styles.table_row}>
                <p className={styles.row_title}>Доп. информация</p>

                <OutlinedInput
                  onChange={handleChangeInput}
                  name="addition_info"
                  value={formData.addition_info}
                  className={styles.input_block}
                  sx={{ width: "282px" }}
                />
              </div>
            </div>

            <div className={styles.table_row}>
              <p className={styles.row_title}>Примечание рег</p>

              <OutlinedInput
                className={styles.input_block}
                sx={{ width: "339px" }}
              />
            </div>

            <div className={styles.table_row}>
              <Button variant="outlined" className={styles.button_white}>
                Допольнительно
              </Button>
              <Button variant="outlined" className={styles.button_white}>
                Аптека
              </Button>
              <FormControlLabel
                control={<Checkbox />}
                name="isContract"
                onChange={handleChangeInput}
                label="Контракты"
                className={styles.checkbox_block}
              />
            </div>

            <div className={styles.table_title}>Дополнительно</div>
            <div className={styles.table_wrapper}>
              <div className={styles.table_row}>
                <p className={styles.row_title}>№ контракта</p>

                <FlexSpaceBetween sx={{ width: "331px" }}>
                  <Autocomplete
                    disablePortal
                    sx={{ width: "234px" }}
                    id="combo-box-demo"
                    options={[
                      {
                        label: "test",
                      },
                      {
                        label: "test2",
                      },
                      {
                        label: "test3",
                      },
                    ]}
                    className={styles.input_block}
                    noOptionsText={"Контракт не найдено"}
                    renderInput={(params) => (
                      <TextField
                        {...params}
                        label="Виберите номер контракта"
                        InputLabelProps={{
                          sx: [
                            {
                              top: "-12px",
                              fontSize: "14px",
                            },
                            {
                              "&.Mui-focused": {
                                top: 0,
                              },
                            },
                          ],
                        }}
                      />
                    )}
                  />

                  <Button
                    variant="outlined"
                    className={styles.button_white}
                    sx={{ width: "87px !important" }}
                  >
                    Лимиты
                  </Button>
                </FlexSpaceBetween>
              </div>

              <div className={styles.table_row}>
                <p className={styles.row_title}>№ полиса</p>

                <OutlinedInput
                  className={styles.input_block}
                  sx={{ width: "332px" }}
                />
              </div>

              <div className={styles.table_row}>
                <p className={styles.row_title}>Выбрать очередь</p>

                <Autocomplete
                  disablePortal
                  sx={{ width: "333px" }}
                  id="combo-box-demo"
                  options={[
                    {
                      label: "test",
                    },
                    {
                      label: "test2",
                    },
                    {
                      label: "test3",
                    },
                  ]}
                  className={styles.input_block}
                  noOptionsText={"Очередь не найдено"}
                  renderInput={(params) => (
                    <TextField
                      {...params}
                      label="Очередь"
                      InputLabelProps={{
                        sx: [
                          {
                            top: "-12px",
                          },
                          {
                            "&.Mui-focused": {
                              top: 0,
                            },
                          },
                        ],
                      }}
                    />
                  )}
                />
              </div>

              <div className={styles.table_row}>
                <FormControlLabel
                  control={<Checkbox />}
                  label="Поставить вне очереди"
                  className={styles.checkbox_block}
                />
                <FormControlLabel
                  control={<Checkbox />}
                  label="Отправить смс оповещение"
                  className={styles.checkbox_block}
                />
              </div>
            </div>
          </div>
          <div className={styles.right_table}>
            <div className={styles.table_title}>Услуги</div>
            <div className={styles.table_wrapper}>
              <div className={styles.left_side}>
                <div className={styles.top_box}>
                  <p>Выбранные услуги</p>
                </div>
                <div className={styles.list_block}>
                  <div className={styles.list_top}>
                    <div className={styles.list_top_item}>Название</div>
                    <div className={styles.list_top_item}>Количество</div>
                    <div className={styles.list_top_item}>Удалить</div>
                    <div className={styles.list_top_item}>Стоимост</div>
                    <div className={styles.list_top_item}>Скидки</div>
                  </div>
                  <div className={styles.list_wrapper}>
                    <table>
                      <tbody>
                        {appointedServices.map((appointedService, index) => (
                          <tr key={index}>
                            <td>{appointedService.service.name}</td>
                            <td className={styles.center_cel}>
                              {appointedService.quantity}
                            </td>
                            <td>
                              <div
                                className={styles.icon_cell}
                                onClick={() => {
                                  appointedService.quantity--;
                                  if (appointedService.quantity) {
                                    setAppointedServices([
                                      ...appointedServices,
                                    ]);
                                  } else {
                                    setAppointedServices((prevState) => [
                                      ...prevState.filter(
                                        (prev) =>
                                          prev.service.id !==
                                          appointedService.service.id
                                      ),
                                    ]);
                                  }
                                }}
                              >
                                <CloseCircle />
                              </div>
                            </td>
                            <td className={styles.center_cel}>
                              {new Intl.NumberFormat().format(
                                appointedService.service.cost *
                                appointedService.quantity *
                                (1 - discount / 100)
                              )}{" "}
                              UZS
                            </td>
                            <td className={styles.center_cel}>{discount} %</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
              <div className={styles.right_side}>
                <div className={styles.top_box}>
                  <p>Поиск услуг</p>

                  <input
                    type="text"
                    className={styles.input_top_block}
                    value={serviceSearchText}
                    onChange={(event) =>
                      setServiceSearchText(event.target.value)
                    }
                  />
                </div>

                <div className={styles.list_block}>
                  <div className={styles.list_top}>
                    <div className={styles.list_top_item}></div>
                    <div className={styles.list_top_item}>Название</div>
                    <div className={styles.list_top_item}>Цена</div>
                  </div>

                  <div className={styles.list_wrapper}>
                    <table>
                      <tbody>
                        {services
                          .filter((service) =>
                            service.name
                              .toLowerCase()
                              .includes(serviceSearchText.toLowerCase())
                          )
                          .map((service, i) => (
                            <tr key={i}>
                              <td style={{ padding: 0 }}>
                                <div
                                  className={`${styles.icon_cell} ${styles.green}`}
                                  onClick={() => {
                                    let found = false;
                                    appointedServices.forEach(
                                      (appointedService) => {
                                        if (
                                          appointedService.service.id ===
                                          service.id
                                        ) {
                                          found = true;
                                          appointedService.quantity++;
                                          setFormData({
                                            ...formData,
                                            debt:
                                              appointedService.service.cost *
                                              appointedService.quantity,
                                          });
                                        }
                                      }
                                    );
                                    if (found) {
                                      setAppointedServices([
                                        ...appointedServices,
                                      ]);
                                    } else {
                                      setAppointedServices((prevState) => [
                                        ...prevState,
                                        {
                                          quantity: 1,
                                          service: service,
                                          discount: discount,
                                        },
                                      ]);
                                    }
                                  }}
                                >
                                  <AddCircle />
                                </div>
                              </td>
                              <td>{service.name}</td>
                              <td>
                                {new Intl.NumberFormat().format(service.cost)}{" "}
                                UZS
                              </td>
                            </tr>
                          ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </>
    );
  }
);

export default PatientsTable;
