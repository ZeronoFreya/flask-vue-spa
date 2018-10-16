<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {};
    },
    methods: {
        getSelectFolderList() {
            const path = 'http://localhost:5000/api/dl/listdir2';
            axios
                .post(path,{
                    rootDir:'f:\\Project\\Python',
                    idx:2
                })
                .then(response => {
                    // this.randomNumber = response.data.randomNumber;
                    console.log(response.data)
                })
                .catch(error => {
                    console.log(error);
                });
        },
    },
    created() {
        this.getSelectFolderList();
    },
};
</script>

