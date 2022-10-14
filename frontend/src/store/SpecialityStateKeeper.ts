import {makeAutoObservable, runInAction} from "mobx";
import {SpecialityApiStub} from "../repositories";
import {ISpeciality} from "../consts/types";

class SpecialityStateKeeper {

    static _instance: SpecialityStateKeeper;
    private readonly specialityApiStub: SpecialityApiStub;

    specialities: ISpeciality[] = [];

    static get instance() {
        if (!SpecialityStateKeeper._instance) {
            SpecialityStateKeeper._instance = new SpecialityStateKeeper();
        }
        return SpecialityStateKeeper._instance;
    }

    constructor(
        specialtyApiStub: SpecialityApiStub = SpecialityApiStub.instance
    ) {
        this.specialityApiStub = specialtyApiStub;
        makeAutoObservable(this, {}, {autoBind: true});
    }

    async findAllSpecialties(): Promise<ISpeciality[]> {
        const specialties = await this.specialityApiStub.findAllSpecialties();
        runInAction(() => {
            this.specialities = specialties;
        });
        return specialties;
    }

}

export default SpecialityStateKeeper;

