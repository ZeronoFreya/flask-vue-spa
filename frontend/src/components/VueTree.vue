<template>
  <ul class="vue-tree-list">
    <tree-item
      v-for="(item, idx) in treeData"
      :ids="ids"
      :ids-with-parent="idsWithParent"
      :model="item"
      :options="termOptions"
      :depth="0"
      :state="state"
      :key="idx"
      @handle="handle"
    />
  </ul>
</template>
<style lang="postcss">
    .vue-tree-list {
        list-style-type: none;
        padding-left: 20px;
        .item-wrapper {
            padding: 5px 0;
            height: 100%;
            line-height: 100%;
        }
        .item-bold {
           font-weight: bold
        }
        .item-toggle,
        .item-checkbox,
        .item-label {
          cursor: pointer;
        }
        .item-toggle {
            vertical-align: top;
            display: inline-block;
            width: 20px;
            text-align: center;
            overflow: hidden
        }
    }
</style>
<script>
  import Item from './Item.vue'
  // import '../assets/css/vue-tree.css'

  export default {
    components: { 'tree-item': Item },

    model: {
      prop: 'ids',
      event: 'change'
    },

    props: {
      treeData: {
        type: Array,
        default: function () {
          return []
        }
      },
      options: {
        type: Object,
        default: function () {
          return {}
        }
      },
      ids: {
        type: Array,
        default: function () {
          return []
        }
      }
    },

    data () {
      return {
        defaultOptions: {
          label: 'label',
          checkbox: true,
          checkedOpen: true,
          folderBold: true,
          idsWithParent: true,
          depthOpen: 0,
          openIcon: ['fa','angle-right'],
          closeIcon: ['fa','angle-down'],
          halfCheckedIcon: ['fab', 'twitter-square'],
          checkedIcon: ['far', 'check-square'],
          uncheckedIcon: ['far','square']
        },
        termOptions: {},
        idsWithParent: [],
        state: 0
      }
    },

    created () {
      this.initOptions()
      this.idsWithParent = this.ids.slice(0)
    },

    watch: {
      options: {
        handler: function (val) {
          this.initOptions()
        },
        deep: true
      }
    },

    methods: {
      handle (item) {
        console.log(2)
        this.$emit('handle', item)
      },
      initOptions () {
        this.termOptions = Object.assign({}, this.defaultOptions, this.options)
        this.idsWithParent = this.ids.slice(0)
      }
    }
  }
</script>
