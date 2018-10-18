import Vue from "vue";
import App from "./App.vue";
import router from "./router";

import { library } from "@fortawesome/fontawesome-svg-core";
// import { faCoffee } from "@fortawesome/free-solid-svg-icons";
import { faPlusSquare, faMinusSquare, faFolder, faFolderOpen, faFile } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faPlusSquare);
library.add(faMinusSquare);
library.add(faFolder);
library.add(faFolderOpen);
library.add(faFile);

Vue.component("font-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
    router,
    render: h => h(App),
}).$mount("#app");
