import {Component, OnInit, ViewContainerRef} from '@angular/core';
import {FileUploader} from 'ng2-file-upload'
import {User} from './users/models/user';
import {UserService} from './users/services/user.service';
import {ProfileService} from './profiles/services/profile.service';
import {Overlay} from 'angular2-modal';
import {Modal} from 'angular2-modal/plugins/bootstrap';

@Component({
    selector: 'profile-edit',
    templateUrl: './profile-edit.component-old.html',
    styleUrls: [
        './profile-edit.component.css'
    ]
})

export class ProfileEditComponent implements OnInit {

    model: User;
    submitted = false;
    uploader: FileUploader;

    constructor(
        private userService: UserService,
        private profileService: ProfileService,
        public modal: Modal,
        overlay: Overlay,
        vcRef: ViewContainerRef
    ) {
        overlay.defaultViewContainer = vcRef;
    }

    ngOnInit(): void {
        this.initUser();
        this.initUploader();
    }

    initUploader() {
        var self = this;

        var uploader = new FileUploader({
            url: '/api/v1.0/uploads/',
            autoUpload: true,
            removeAfterUpload: true
        });

        uploader.onCompleteItem = function (item, response: string, status: number) {
            var json = JSON.parse(response);
            self.model.profile.imageLink = json.data.attributes.link;
            self.model.profile.image = json.data.uuid;
        };

        self.uploader = uploader;
    }

    onSubmit() {
        var self = this;
        this.submitted = true;

        var attrs = {
            first_name: self.model.profile.firstName,
            last_name: self.model.profile.lastName,
            image: self.model.profile.image,
            birth_date: self.model.profile.birthDate
        };

        this.profileService
            .putCurrent(self.model.profile.uuid, {
                first_name: self.model.profile.firstName,
                last_name: self.model.profile.lastName,
                image: self.model.profile.image,
                birth_date: null
            })
            .then(profile => {
                console.log('vasya');
                self.modal.alert()
                .size('lg')
                .showClose(true)
                .title('Good')
                .open();
            });
    }

    initUser() {
        this.userService
            .getCurrent()
            .then(user => {
                this.model = user;
            });
    }

}