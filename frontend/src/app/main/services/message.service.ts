import {Injectable} from '@angular/core';

import 'rxjs/add/operator/toPromise';
import {ToastyService, ToastyConfig} from "ng2-toasty";


@Injectable()
export class MessageService {

    constructor(
        private toastySrv: ToastyService,
        private toastyConfig: ToastyConfig
    ) {
        this.initDefaultConfig();
    }

    success(msg: string) {
        this.toastySrv.success(msg);
    }

    error(msg: string) {
        this.toastySrv.error(msg);
    }


    private initDefaultConfig() {
         this.toastyConfig.theme = 'bootstrap';
    }

}