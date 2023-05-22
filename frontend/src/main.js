import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import './assets/css/global.css'

axios.defaults.baseURL = 'http://localhost:8000';

const app = createApp(App);
app.config.globalProperties.$http = axios;

app.mount('#app');
