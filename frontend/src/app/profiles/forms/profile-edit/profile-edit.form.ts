import {Component, Input, OnInit} from '@angular/core';
import {FileUploader} from 'ng2-file-upload'
import {FormBuilder, FormGroup} from '@angular/forms';
import {ProfileService} from '../../services/profile.service';
import {User} from '../../../users/models/user';
import {MessageService} from "../../../main/services/message.service";
import {ResponseError} from "../../../main/models/errors";

@Component({
    selector: 'profile-edit-form',
    templateUrl: 'profile-edit.form.html',
    styleUrls: [
        'profile-edit.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class ProfileEditForm implements OnInit {

    @Input()
    user: User;

    form: FormGroup;
    uploader: FileUploader;
    imagePreview: string;

    constructor(
        private fb: FormBuilder,
        private profileSrv: ProfileService,
        private msgSrv: MessageService,
    ) {}

    ngOnInit(): void {
        this.initForm();
        this.initUploader();
    }

    initForm() {
        this.form = this.fb.group({
            first_name: [this.user.profile.firstName],
            last_name: [this.user.profile.lastName],
            birth_date: [this.user.profile.birthDate],
            image: [this.user.profile.image],
        });
    }

    initUploader() {
        let _this = this;
        let uploader = new FileUploader({
            url: '/api/v1.0/uploads/profile-images',
            autoUpload: true,
            removeAfterUpload: true
        });

        uploader.onCompleteItem = function (item: any, response: string, status: number) {
            let json = JSON.parse(response);
            _this.imagePreview = json.link;
            _this.form.patchValue({'image': json.id});
        };

        _this.uploader = uploader;
        _this.imagePreview = _this.user.profile.imageLink;
    }

    onSubmit() {
        let values = this.form.value;
        this.profileSrv
            .putCurrent(values)
            .then(profile => this.msgSrv.success('Profile settings successfully saved.'))
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}