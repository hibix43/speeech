<template>
  <div id="index">
    <DataManager :inputTexts="texts" ref="manager"></DataManager>
    <Canvas :inputTexts="texts"></Canvas><br>
    <textarea v-model="texts" placeholder="input here"/><br>
    <button type="submit" @click="prevSlide">前のスライドへ</button>
    <button type="submit" @click="nextSlide">次のスライドへ</button>
    <!--<input type="range" min="0" v-bind:max="slideLength" step="1" v-model="number">-->
    <p>texts: {{ texts }}</p>
    <p>slideNum: {{ slideNum }}</p>
    <p>slideLength: {{ slideLength }}</p>
  </div>
</template>

<script>
import DataManager from './DataManager.vue'
import Canvas from './Canvas.vue'
export default {
  components: {
    DataManager,
    Canvas
  },
  data () {
    return {
      texts: '',
      slideNum: 0,
      slideLength: 0
    }
  },
  methods: {
    nextSlide () {
    },
    prevSlide () {
    }
  }
}
</script>
