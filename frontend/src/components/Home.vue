
<template>
  <div>
      <a href="#">hr <span class="child1">wwww</span></a>
    <li v-for="(val, key, index) in me">{{index}}. {{key}}: {{val}}</li>
    <button @click="getRandom">New random number</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      randomNumber: 0,
      me: {
        name: 'Dale',
        age: 22,
        sex: 'male',
        height: 170
      }
    }
  },
  methods: {
    getRandomInt (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandom () {
      // this.randomNumber = this.getRandomInt(1, 100)
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
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
  created () {
    this.getRandom()
  }
}
</script>

<style lang="postcss" scoped>
    a {
        color: red;
        font-size: 14px;
        .child1 {
            color: green;
        }
        &.active {
            font-weight: bold;
        }
        &:hover {
            font-size: 18px;
        }
    }
</style>
