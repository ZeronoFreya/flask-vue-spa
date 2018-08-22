
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
  <ul>
    <li v-for="(val, key, index) in listdir">{{val}}</li>
  </ul>
  <vue-tree
    v-model="checkedIds"
    :tree-data="treeData"
    :options="options"
    @handle="someActions" />
  <!-- <button @click="getRandom">New random number</button> -->
</div>
</template>

<script>
import axios from 'axios'
import VueTree from './VueTree.vue'
export default {
  components: { VueTree },
  data() {
    return {
      // 复选ids,可传入id数组作为初始选中状态,如[3,4,8]
      checkedIds: [],
      treeData: [],
      options: {
          depthOpen: 1,          //初始化时展开层级,根节点为0,默认0
          openIcon: ['far','folder'],
          closeIcon: ['far','folder-open'],
      },
      randomNumber: 0,
      link: {
        NextCloud: this.getUrl('8888')
      },
      listdir: []
    }
  },
  methods: {
    getUrl(port) {
      const host = 'http://108.61.87.215'
      return host + ":" + port
    },
    getDirList() {
      let rootDir = 'e:$DownLoad$0';
      const path = `http://localhost:5000/api/dl/listdir/` + rootDir + '/1'
      console.log(path)
      axios.get(path)
        .then(response => {
          this.treeData = response.data.listdir
          // console.log(response.data.listdir)
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
    },
    someActions (item) {
        // console.log(`节点 ${JSON.stringify(item)} 'handle' 事件`)
        // console.log(item)
        console.log(3)
    },
    getchild (rootDir) {
        console.log(3)
        rootDir = `http://localhost:5000/api/dl/listdir/` + rootDir + '/20'
        axios.get(rootDir)
          .then(response => {
            // this.treeData = response.data.listdir
            console.log(response.data.listdir)
            // children = response.data.listdir
            this.$root.eventHub.$emit('eventName2', response.data.listdir)
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
  created() {
    this.getDirList()
    this.$root.eventHub.$on('eventName',(rootDir) => {
        this.getchild(rootDir)
    })
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
