import Vue from '../lib/vue.js';

import { ToolsService } from '../services/toolsService.js';

let AppHeader = Vue.component('app-header', {
  	template: '<div class="header">'+
        '<div class="menu">'+
          '<div class="menu-item">FEED<span class="title-327" :style="{backgroundColor: logoColor}">BACK</span></div>'+
        '</div>'+
      '</div>',
    data: function () {
        return {
          logoColor: ""          
        }
    },
  	created: function() {
      var self = this;

      self.logoColor = ToolsService.getFromWarmColors();
      
    }

})

export { AppHeader };
