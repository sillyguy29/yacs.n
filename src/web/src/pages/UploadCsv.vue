<template>
  <b-container>
    <section id="import-data">
      <h2>Import Data</h2>
      <div class="well well-sm">
        Input course data as CSV, for more info, see:
        <a href="#">http://help.com</a>
        (show github link for more docs later)
      </div>
      <form @submit.prevent="onSubmit" class="form-group">
        <div class="input-group">
          <label>
            Upload CSV file
            <input type="file" name="file" class="form-control-file" />
          </label>
          <br />
        </div>
        <div class="input-group">
          <label>
            <input type="checkbox" name="is_publicly_visible" checked />
            Make Public
          </label>
        </div>
        <input
          type="Submit"
          label="submit"
          class="btn btn-success btn-sm"
          value="Submit"
        />
      </form>
    </section>
    <b-spinner v-show="loading" />
  </b-container>
</template>

<script>
import { uploadCsv } from "@/services/AdminService";

export default {
  name: "UploadCsv",
  components: {},
  props: {},
  data() {
    return {
      loading: false,
      isPublic: false,
    };
  },
  methods: {
    onSubmit(event) {
      if (!this.loading) {
        let formData = new FormData(event.target);
        this.loading = true;
        this.$emit("loading");
        if (formData.get("file") && formData.get("file").name) {
          let filename = formData.get("file").name;
          uploadCsv(formData)
            .then((response) => {
              console.log(response);
              // Axios will only enter this block if the status code is 2xx,
              // so handle errors for catch block. https://stackoverflow.com/questions/49967779/axios-handling-errors
              this.$bvToast.toast(
                `${filename} has been successfully uploaded!`,
                {
                  title: "Upload Result",
                  variant: "info",
                  noAutoHide: false,
                }
              );
              this.loading = false;
              this.$emit("loadfinish");
            })
            .catch((error) => {
              console.log(error.response);
              this.loading = false;
              this.$emit("loadfinish");
              this.$bvToast.toast(
                `HTTP ${error.response.status}: ${error.response.data}`,
                {
                  title: "Upload Result",
                  variant: "danger",
                  noAutoHide: true,
                }
              );
            });
        } else {
          this.$bvToast.toast(`Must upload a CSV file`, {
            title: "Validation Error",
            variant: "danger",
            noAutoHide: false,
          });
          this.loading = false;
          this.$emit("loadfinish");
        }
      }
    },
    back() {
      window.history.back();
    },
  },
};
</script>

<style lang="scss" scoped></style>
