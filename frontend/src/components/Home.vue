
<template>
<div>
  <ul>
    <li class="nav" v-for="(val, key, index) in link">
      <!-- <router-link :name="key" :to="val">{{key}}</router-link> -->
      <a :href="val" target="_blank">
          <img src="https://avatars0.githubusercontent.com/u/19211038?s=200&v=4" :alt="key">
      </a>
      <p>{{key}}</p>
    </li>
  </ul>
  <!-- <button @click="getRandom">New random number</button> -->
</div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      randomNumber: 0,
      link: {
        NextCloud: this.getUrl('8888')
      },
      listdir: []
    }
  },
  methods: {
    getUrl(port) {
      const host = 'http://108.61.87.215';
      return host + ":" + port;
    },
    getDirList() {
      const path = `http://localhost:5000/api/listdir`
      axios.get(path)
        .then(response => {
          this.listdir = response.data.listdir
          console.log(response.data.listdir)
        })
        .catch(error => {
          console.log(error)
        })
    },
    getRandomInt(min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandom() {
      // this.randomNumber = this.getRandomInt(1, 100)
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend() {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created() {
    this.getDirList()
  }
}
</script>

<style lang="postcss" scoped>
    li.nav{
        width: 100px;
        a{
            display:block;
            width: 100px;
            height: 100px;
            border: 1px #ccc solid;
            border-radius: 5px;
            overflow: hidden;
        }
        img{
            width: 100%;
            height: 100%;
        }
        p{
            text-align: center;
        }
    }
</style>
