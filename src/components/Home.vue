<template>
  <div class="container">
    <page-header />
    <chart />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Chart from "@/components/Chart";
import PageHeader from "@/components/PageHeader";

export default Vue.extend({
  components: {Chart, PageHeader},
});
</script>

<style>
html {
  background: #fafcff;
}

button: {
  user-select: none;
}
</style>

<style scoped>
.container {
  margin-top: 132px;
}
</style>
