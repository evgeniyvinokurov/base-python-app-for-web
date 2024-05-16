import Vue from '../lib/vue.js';

let AppFooter = Vue.component('app-footer', {
  	template: '<div class="footer">'+
          '<div class="menu">'+
            '<div class="menu-item"><a href="http://hot-cloth.surge.sh/">Винокуров Е.А.</a></div>'+
          '</div>'+
          '<div class="menu">'+
            '<div class="menu-item"><a href="https://gitflic.ru/project/evgeniyvinokurov">Gitflick</a></div>'+
          '</div>'+
          ''+
      '</div>',
    data: function () {
        return {
          data: ""
        }
    },
  	created: function() {
    },
    methods: {

    }
})

export { AppFooter };
