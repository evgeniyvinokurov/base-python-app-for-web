import { AjaxService } from './ajaxService.js';

let UsersService = {  
  checkpost: function(cb, user){
    let fdata = new FormData();
    
    fdata.append("name", user["name"]);
    fdata.append("phone", user["phone"]);
    fdata.append("comment", user["comment"]);
    fdata.append("email", user["email"]);

    AjaxService.doAjaxPost("/user/checkpost/", fdata, function(data){
        cb(data);
    })
  }
}

export { UsersService };
