import {Body} from '@angular/http/src/body';
import {Injectable} from '@angular/core';

@Injectable()
export class ResponseService {

    parseData(response: Body): any {
        return response.json();
    }

    parseErrors(response: Body): Array<any> {
        return response.json().errors;
    }

}