<template>
  <div id="index">
    <Canvas :inputTexts="texts" ref="canvas"></Canvas>
    <textarea v-model="texts" placeholder="ここに入力してスライドを作成しよう"/>
    <p class="page-num">{{ index+1 }}番目のスライドを表示中</p>
    <div class="row">
      <button class="btn six columns" type="submit" @click="prevSlide">前のスライドへ</button>
      <button class="btn six columns" type="submit" @click="nextSlide">次のスライドへ</button>
    </div>
    <div class="row">
      <button class="btn four columns" type="submit" @click="startAnimation(0)">最初のスライドから再生</button>
      <button class="btn four columns" type="submit" @click="startAnimation(index)">現在のスライドから再生</button>
      <button class="btn four columns" type="submit" @click="stopAnimation">停止</button>
    </div>
    <input type="text" size="100" v-model="inputTweet" placeholder="ツイート内容を入力"/>
    <button class="btn complete-btn" type="submit" @click="createGif">完成させてツイートする</button>
    <div>{{ backendMsg }}</div>
    <img class="gif-img" v-bind:src="gifURL" width="400"/>
    <DataManager :inputTexts="texts" ref="manager"></DataManager>
  </div>
</template>

<script>
import axios from 'axios'
import DataManager from './DataManager.vue'
import Canvas from './Canvas.vue'
export default {
  components: {
    DataManager,
    Canvas
  },
  data () {
    return {
      index: 0,
      texts: '',
      gifURL: '',
      inputTweet: '',
      backendMsg: ''
    }
  },
  watch: {
    index () {
      this.texts = this.$refs.manager.getSlideTexts(this.index)
    }
  },
  methods: {
    setSlideTexts () {
      if (this.texts !== '' && this.texts !== undefined) {
        this.$refs.manager.setSlideTexts(this.index)
      }
    },
    nextSlide () {
      if (this.texts !== '' && this.texts !== undefined && this.index < this.$refs.manager.getSlides().length) {
        this.setSlideTexts()
        this.index += 1
      }
      this.texts = this.$refs.manager.getSlideTexts(this.index)
    },
    prevSlide () {
      this.setSlideTexts()
      if (this.index > 0) {
        this.index -= 1
      }
      this.texts = this.$refs.manager.getSlideTexts(this.index)
    },
    startAnimation (startIndex) {
      this.setSlideTexts()
      this.$refs.canvas.startAnimation(this.$refs.manager.getSlides(), startIndex)
    },
    stopAnimation () {
      this.$refs.canvas.stopAnimation()
    },
    createGif () {
      const base64URL = 'data:image/gif;base64,'
      this.setSlideTexts()
      this.gifURL = base64URL + this.$refs.canvas.createGif(this.$refs.manager.getSlides())
      this.postTweet()
    },
    postTweet () {
      const that = this
      axios.post('/tweet', {
        'img': this.gifURL,
        'msg': this.inputTweet
      })
        .then(
          function (response) {
            that.backendMsg = response.data.message
          }
        )
    }
  }
}
</script>

<style scoped>
#index {
  position: relative;
  height: auto;
  min-height: 100%;
  background-color: #fff;
}
textarea {
  min-width: 320px;
  width: 90%;
  max-width: 600px;
  min-height: 180px;
  margin: 16px 0;
  border: 4px solid #ddd;
}
.row {
  margin: 16px 64px;
}
.btn {
  font-size: 1em;
  font-weight: bold;
  background-color: #666;
  color: #fff;
}
.complete-btn {
  font-size: 1.5em;
  border-radius: 0;
  margin: 8px 0;
  width: 320px;
  height: 60px;
  background-color: #00bbee;
  color: #fff;
  border: 1px solid #fff;
  box-shadow: 0 0 4px #00bbee;
}
.gif-img {
  display: block;
  margin-top: 40px;
  padding-bottom: 100px;
}
.page-num {
  width: 200px;
  padding: 8px;
  color: #999;
  border: 4px double #ccc;
}
</style>
