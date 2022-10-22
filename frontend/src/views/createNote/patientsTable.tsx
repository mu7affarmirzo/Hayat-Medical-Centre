import React from 'react';
import styles from "./index.module.scss";
import {
    Autocomplete, Button,
    Checkbox,
    FormControl,
    FormControlLabel,
    InputLabel,
    MenuItem, OutlinedInput,
    Select,
    TextField
} from "@mui/material";
import {DesktopDatePicker, TimePicker} from "@mui/x-date-pickers";
import CurrencyInput from "react-currency-input-field";
import {FlexSpaceBetween} from "../../themes/customItems";
import {ReactComponent as CloseCircle} from "../../assets/img/close-circle.svg";
import {ReactComponent as AddCircle} from "../../assets/img/add-circle.svg";

const PatientsTable = ({
                           selectData,
                           setSelectData,
                           timeValue,
                           dateValue,
                           setDateValue,
                           timeChangeHandler
                       }) => {
    return (
        <>
            <div className={styles.patients_main_table}>
                <div className={styles.left_table}>
                    <div className={styles.table_title}>Детали</div>
                    <div className={styles.table_wrapper}>

                        <div className={styles.table_wrapper_block}>
                            <div className={styles.table_row}>
                                <p className={styles.row_title}>Льгота</p>

                                <FormControl className={styles.table_dropdown} >
                                    <InputLabel
                                        id="demo-simple-select-label"
                                        sx={[
                                            {
                                                top: "-12px",
                                                fontSize: "14px",
                                            },
                                            {
                                                "&.Mui-focused": {
                                                    top: 0
                                                }
                                            }
                                        ]}
                                    >
                                        Без скидок
                                    </InputLabel>
                                    <Select
                                        labelId="demo-simple-select-label"
                                        id="demo-simple-select"
                                        value={selectData}
                                        label="Без скидок"
                                        onChange={(e) => setSelectData(e.target.value)}
                                        sx={{height: "32px"}}
                                    >
                                        <MenuItem value={"head1"}>Головной1</MenuItem>
                                        <MenuItem value={"head2"}>Головной2</MenuItem>
                                        <MenuItem value={"head3"}>Головной3</MenuItem>
                                    </Select>
                                </FormControl>
                            </div>
                        </div>

                        <div className={styles.table_wrapper_block}>
                            <div className={styles.table_row}>
                                <p className={styles.row_title} style={{marginRight: "17px"}}>Дата приема</p>

                                <DesktopDatePicker
                                    label="Выберете дату"
                                    inputFormat="DD/MM/YYYY"
                                    className={styles.input_block}
                                    value={dateValue}
                                    onChange={setDateValue}
                                    renderInput={(params) => <TextField {...params} sx={{width: "270px", marginRight: "25px"}} />}
                                />

                                <FormControlLabel control={<Checkbox />} label="Авто" className={styles.checkbox_block}/>
                            </div>

                            <div className={styles.table_row}>
                                <p className={styles.row_title} style={{marginRight: "10px"}}>Время начала</p>

                                <TimePicker
                                    label="Time"
                                    value={timeValue.from}
                                    className={styles.input_block}
                                    onChange={(newValue) => timeChangeHandler(newValue, "from")}
                                    renderInput={(params) => <TextField {...params}  sx={{width: "103px", marginRight: "15px"}} />}
                                />

                                <p className={styles.row_title} style={{marginRight: "10px"}}>Время завершения</p>

                                <TimePicker
                                    label="Time"
                                    value={timeValue.to}
                                    className={styles.input_block}
                                    onChange={(newValue) => timeChangeHandler(newValue, "to")}
                                    renderInput={(params) => <TextField {...params}  sx={{width: "103px"}} />}
                                />
                            </div>
                        </div>

                        <div className={styles.table_wrapper_block}>
                            <div className={styles.table_row}>
                                <p className={styles.row_title} style={{marginRight: "30px"}}>Долг</p>

                                <CurrencyInput
                                    id="input-example"
                                    name="input-name"
                                    placeholder="Please enter a number"
                                    defaultValue="0"
                                    allowDecimals={true}
                                    allowNegativeValue={false}
                                    prefix="UZS "
                                    className={styles.currency_input}
                                    onValueChange={(value, name) => console.log(value, name)}
                                />
                            </div>

                            <div className={styles.table_row}>
                                <p className={styles.row_title} style={{marginRight: "24px"}}>Итого</p>

                                <CurrencyInput
                                    id="input-example"
                                    name="input-name"
                                    placeholder="Please enter a number"
                                    defaultValue="0"
                                    allowDecimals={true}
                                    allowNegativeValue={false}
                                    prefix="UZS "
                                    className={styles.currency_input}
                                    onValueChange={(value, name) => console.log(value, name)}
                                    style={{marginRight: "35px"}}
                                />

                                <FormControlLabel control={<Checkbox />} label="Вручную" className={styles.checkbox_block}/>
                            </div>
                        </div>

                        <div className={styles.table_row}>
                            <p className={styles.row_title}>Направивший врач</p>

                            <Autocomplete
                                disablePortal
                                sx={{width: "282px"}}
                                id="combo-box-demo"
                                options={[
                                    {
                                        label: "test"
                                    },
                                    {
                                        label: "test2"
                                    },
                                    {
                                        label: "test3"
                                    }
                                ]}
                                className={styles.input_block}
                                noOptionsText={'Направление не найдено'}
                                renderInput={(params) => <TextField {...params} label="Выберите направление" InputLabelProps={{
                                    sx: [
                                        {
                                            top: "-12px",
                                            fontSize: "14px",
                                        },
                                        {
                                            "&.Mui-focused": {
                                                top: 0
                                            }
                                        }
                                    ]
                                }} />}
                            />
                        </div>

                        <div className={styles.table_row}>
                            <p className={styles.row_title}>Источники информации</p>

                            <Autocomplete
                                disablePortal
                                sx={{width: "282px"}}
                                id="combo-box-demo"
                                options={[
                                    {
                                        label: "test3"
                                    },
                                    {
                                        label: "test4"
                                    },
                                    {
                                        label: "test5"
                                    }
                                ]}
                                className={styles.input_block}
                                noOptionsText={'Источник не найдено'}
                                renderInput={(params) => <TextField {...params} label="Выберите источники" InputLabelProps={{
                                    sx: [
                                        {
                                            top: "-12px",
                                            fontSize: "14px",
                                        },
                                        {
                                            "&.Mui-focused": {
                                                top: 0
                                            }
                                        }
                                    ]
                                }} />}
                            />
                        </div>

                        <div className={styles.table_row}>
                            <p className={styles.row_title}>Коммент нап врача</p>

                            <OutlinedInput className={styles.input_block} sx={{width: "282px"}}/>
                        </div>

                        <div className={styles.table_row}>
                            <p className={styles.row_title}>Доп. информация</p>

                            <OutlinedInput className={styles.input_block} sx={{width: "282px"}}/>
                        </div>

                    </div>

                    <div className={styles.table_row}>
                        <p className={styles.row_title}>Примечание рег</p>

                        <OutlinedInput className={styles.input_block} sx={{width: "339px"}}/>
                    </div>

                    <div className={styles.table_row}>
                        <Button variant="outlined" className={styles.button_white}>Допольнительно</Button>
                        <Button variant="outlined" className={styles.button_white}>Аптека</Button>
                        <FormControlLabel control={<Checkbox />} label="Контракты" className={styles.checkbox_block}/>
                    </div>

                    <div className={styles.table_title}>Дополнительно</div>
                    <div className={styles.table_wrapper}>
                        <div className={styles.table_row}>
                            <p className={styles.row_title}>№ контракта</p>

                            <FlexSpaceBetween sx={{width: "331px"}}>
                                <Autocomplete
                                    disablePortal
                                    sx={{width: "234px"}}
                                    id="combo-box-demo"
                                    options={[
                                        {
                                            label: "test"
                                        },
                                        {
                                            label: "test2"
                                        },
                                        {
                                            label: "test3"
                                        }
                                    ]}
                                    className={styles.input_block}
                                    noOptionsText={'Контракт не найдено'}
                                    renderInput={(params) => <TextField {...params} label="Виберите номер контракта" InputLabelProps={{
                                        sx: [
                                            {
                                                top: "-12px",
                                                fontSize: "14px",
                                            },
                                            {
                                                "&.Mui-focused": {
                                                    top: 0
                                                }
                                            }
                                        ]
                                    }} />}
                                />

                                <Button variant="outlined" className={styles.button_white} sx={{width: "87px !important"}}>Лимиты</Button>
                            </FlexSpaceBetween>
                        </div>

                        <div className={styles.table_row}>
                            <p className={styles.row_title}>№ полиса</p>

                            <OutlinedInput className={styles.input_block} sx={{width: "332px"}}/>
                        </div>

                        <div className={styles.table_row}>
                            <p className={styles.row_title}>Выбрать очередь</p>

                            <Autocomplete
                                disablePortal
                                sx={{width: "333px"}}
                                id="combo-box-demo"
                                options={[
                                    {
                                        label: "test"
                                    },
                                    {
                                        label: "test2"
                                    },
                                    {
                                        label: "test3"
                                    }
                                ]}
                                className={styles.input_block}
                                noOptionsText={'Очередь не найдено'}
                                renderInput={(params) => <TextField {...params} label="Очередь" InputLabelProps={{
                                    sx: [
                                        {
                                            top: "-12px"
                                        },
                                        {
                                            "&.Mui-focused": {
                                                top: 0
                                            }
                                        }
                                    ]
                                }} />}
                            />
                        </div>

                        <div className={styles.table_row}>
                            <FormControlLabel control={<Checkbox />} label="Поставить вне очереди" className={styles.checkbox_block}/>
                            <FormControlLabel control={<Checkbox />} label="Отправить смс оповещение" className={styles.checkbox_block}/>
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
                                            <tr>
                                                <td>И по сей день в центральных регионах звучит перекатами звон колоколов</td>
                                                <td className={styles.center_cel}>1</td>
                                                <td>
                                                    <div className={styles.icon_cell}>
                                                        <CloseCircle />
                                                    </div>
                                                </td>
                                                <td className={styles.center_cel}>69 647</td>
                                                <td className={styles.center_cel}>0.00</td>
                                            </tr>
                                            <tr>
                                                <td>Прототип нового сервиса — это как треск разлетающихся скреп</td>
                                                <td className={styles.center_cel}>1</td>
                                                <td>
                                                    <div className={styles.icon_cell}>
                                                        <CloseCircle />
                                                    </div>
                                                </td>
                                                <td className={styles.center_cel}>76 602</td>
                                                <td className={styles.center_cel}>0.00</td>
                                            </tr>
                                            <tr>
                                                <td>Зима близко</td>
                                                <td className={styles.center_cel}>1</td>
                                                <td>
                                                    <div className={styles.icon_cell}>
                                                        <CloseCircle />
                                                    </div>
                                                </td>
                                                <td className={styles.center_cel}>96 465</td>
                                                <td className={styles.center_cel}>0.00</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                        <div className={styles.right_side}>
                            <div className={styles.top_box}>
                                <p>Поиск услуг</p>

                                <input type="text" className={styles.input_top_block}/>
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
                                            <tr>
                                                <td style={{padding: 0}}>
                                                    <div className={`${styles.icon_cell} ${styles.green}`}>
                                                        <AddCircle />
                                                    </div>
                                                </td>
                                                <td>И по сей день в центральных регионах звучит перекатами звон колоколов</td>
                                                <td>69 647</td>
                                            </tr>
                                            <tr>
                                                <td style={{padding: 0}}>
                                                    <div className={`${styles.icon_cell} ${styles.green}`}>
                                                        <AddCircle />
                                                    </div>
                                                </td>
                                                <td>И по сей день в центральных регионах звучит перекатами звон колоколов</td>
                                                <td>69 647</td>
                                            </tr>
                                            <tr>
                                                <td style={{padding: 0}}>
                                                    <div className={`${styles.icon_cell} ${styles.green}`}>
                                                        <AddCircle />
                                                    </div>
                                                </td>
                                                <td>И по сей день в центральных регионах звучит перекатами звон колоколов</td>
                                                <td>69 647</td>
                                            </tr>
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
};

export default PatientsTable;