<template>
  <div>
    <canvas width="400" height="300" class="canvas" ref="canvas"></canvas>
  </div>
</template>

<script>
export default {
  props: {
    inputTexts: ''
  },
  data () {
    return {
      animationFlag: false,
      index: 0,
      slides: null
    }
  },
  watch: {
    inputTexts () {
      this.draw(this.inputTexts)
    },
    index () {
      // スライドを描画しきったら、アニメを止める
      if (this.slides[this.index] === '' || this.slides[this.index] === undefined) {
        this.animationFlag = false
      } else {
        // 描画中のindexを親にも反映
        this.$parent.index = this.index
      }
    },
    animationFlag () {
      const self = this
      // アニメーション実行時
      if (this.animationFlag) {
        // 1秒1スライドを描画
        self.animation = setInterval(function () {
          // 描画するテキストを取得
          const showTexts = self.slides[self.index]
          // Index.vue内のtextareaにも反映
          self.$parent.texts = showTexts
          // Canvasに描画
          self.draw(showTexts)
          self.index += 1
        }, 1000)
      } else {
        // 停止
        clearInterval(this.animation)
      }
    }
  },
  methods: {
    draw (texts) {
      const context = this.ctx
      const canvasWidth = 400
      const canvasHeight = 300
      const fontSize = 36
      const lineHeight = 1.2
      let lines = ''

      // 空の場合は表示せず、アニメを止める
      if (this.animationFlag && (texts === '' || texts === undefined)) {
        this.animationFlag = false
        return
      }

      // テキストを改行で分割
      if (texts !== undefined) {
        lines = texts.split('\n')
      }

      // 初期化
      context.width = canvasWidth
      context.height = canvasHeight
      context.clearRect(0, 0, canvasWidth, canvasHeight)
      // 背景色を黒にして塗りつぶす
      context.fillStyle = '#333'
      context.fillRect(0, 0, canvasWidth, canvasHeight)

      // フォント設定
      context.textAlign = 'center'
      context.font = 'bold ' + fontSize + 'px Arial, meiryo, sans-serif'
      context.fillStyle = '#fff'

      // 書きだす
      context.beginPath()

      // 上下中央に描画
      let textsTotalHeight = fontSize * lineHeight * (lines.length - 1) - fontSize / 2.0
      // 行間の高さの分を調整
      if (lines.length > 1) {
        textsTotalHeight -= fontSize * (lineHeight - 1.0)
      }
      // 描画開始高さを決定
      const offset = canvasHeight / 2.0 - textsTotalHeight / 2.0
      // console.log(offset)
      // console.log(canvasHeight - (textsTotalHeight + offset))

      // 改行を反映
      for (let i = 0; i <= lines.length; i++) {
        let line = lines[i]
        let addY = fontSize * lineHeight * i
        if (line !== undefined) {
          // 描画
          context.fillText(line, canvasWidth / 2.0, offset + addY)
        }
      }
    },
    clearContext () {
      this.draw('')
    },
    startAnimation (slides, startIndex) {
      // 初期化
      this.index = startIndex
      this.slides = slides
      // アニメーション始動
      this.animationFlag = true
    },
    stopAnimation () {
      this.animationFlag = false
    },
    createGif (slides) {
      // 初期化
      const GIFEncoder = require('gifencoder')
      let gifAnimation = new GIFEncoder(400, 300)
      gifAnimation.setDelay(500)
      gifAnimation.setRepeat(0)
      gifAnimation.start()
      // 1コマずつ追加
      for (let slide of slides) {
        if (slide !== '' && slide !== undefined) {
          this.draw(slide)
          gifAnimation.addFrame(this.ctx)
        }
      }
      gifAnimation.finish()
      // base64に変換
      return this.convertBase64(gifAnimation)
    },
    convertBase64 (gifAnimation) {
      const binaryGif = gifAnimation.out.getData()
      const base64 = btoa(String.fromCharCode.apply(null, binaryGif))
      // console.log(base64)
      return base64
    }
  },
  mounted () {
    this.ctx = this.$refs.canvas.getContext('2d')
    this.draw(this.inputTexts)
  }
}
</script>

<style scoped>
.canvas {
  width: 90%;
  max-width: 400px;
  margin-top: 24px;
}
</style>
