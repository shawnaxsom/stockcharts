<template>
  <input
    :autofocus='autofocus'
    @keyup.enter='onKeyUp'
    :placeholder='placeholder'
    ref="textField"
    :value="value"
    @input="updateText()"
  />
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "PrimaryButton",
  props: [
    "autofocus",
    "model",
    "onKeyUp",
    "placeholder",
    "value",
  ],
  data: () => {
    return {
      isActive: false,
    };
  },
  methods: {
    updateText() {
      this.$emit('input', this.$refs.textField.value)
    }
  }
});
</script>

<style scoped>
input {
  height: 25px;
  min-width: 150px;
  border: none;
  background: #f8f8f8;
  box-shadow: inset 1px 1px 1px #ccc;
  font-size: 1.03em;
}
</style>
