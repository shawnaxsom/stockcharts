<template>
  <button
    @click="onClick"
    @mouseup="onMouseUp"
    @mousedown="onMouseDown"
    v-bind:class="{ active: isActive }"
  >
      <slot>Button</slot>
  </button>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "SecondaryButton",
  props: ["onClick"],
  data: () => {
    return {
      isActive: false,
    };
  },
  methods: {
    onMouseUp: function() {
      this.isActive = false;
    },
    onMouseDown: function() {
      this.isActive = true;
    }
  }
});
</script>

<style scoped>
button {
  border: none;
  border-radius: 0.8em;
  box-shadow: 0px 0px 3px #2040f0;

  padding: 8px 16px;
  background-color: white;
  color: #2040c0;
  font-size: 1.1em;
  user-select: none;
  outline: none;
}

.active {
  color: #f5f5f5;
  box-shadow: inset 2px 2px 1px #555, inset -2px -2px 8px #2020f0;
}
</style>

