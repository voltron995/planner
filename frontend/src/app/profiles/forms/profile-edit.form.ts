import {Component, Input, OnInit} from '@angular/core';
import {FileUploader} from 'ng2-file-upload'
import {FormBuilder, FormGroup} from '@angular/forms';
import {ProfileService} from '../services/profile.service';
import {User} from '../../users/models/user';

@Component({
    selector: 'profile-edit-form',
    templateUrl: './profile-edit.form.html',
    styleUrls: [
        './profile-edit.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class ProfileEditForm implements OnInit {

    @Input() user: User;
    form: FormGroup;
    uploader: FileUploader;
    imagePreview: string;

    constructor(
        private fb: FormBuilder,
        private profileService: ProfileService
    ) {

    }

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
        var _this = this;
        var uploader = new FileUploader({
            url: '/api/v1.0/uploads/profile-images',
            autoUpload: true,
            removeAfterUpload: true
        });

        uploader.onCompleteItem = function (item: any, response: string, status: number) {
            var json = JSON.parse(response);
            _this.imagePreview = json.link;
            _this.form.patchValue({'image': json.uuid});
        };

        _this.uploader = uploader;
        _this.imagePreview = _this.user.profile.imageLink;
    }

    onSubmit() {
        console.log('submit');
        let values = this.form.value;
        this.profileService
            .putCurrent(values)
            .then(profile => console.log(profile, 'success'))
            .catch(errors => console.log(errors, 'errors'));
    }

}