<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div
        class="modal modal-content"
        role="dialog"
        aria-labelledby="modalTitle"
        aria-describedby="modalDescription"
      >
        <header class="modal-header text-white bg-dark" id="modalTitle">
          <slot name="header">
            {{ titulo }}
            <button
              type="button"
              class="btn-close"
              @click="close"
              aria-label="Close modal"
            >
              x
            </button>
          </slot>
        </header>
        <section class="modal-body">
          <slot name="body">
            <div class="form-group">
              <label class="bold">Nombre: </label>
              <input
                type="text"
                class="form-control"
                v-model="datosAutor.nombre"
              />
            </div>
            <div class="form-group">
              <label class="bold">Documento: </label>
              <input
                type="text"
                class="form-control"
                v-model="datosAutor.dni"
              />
            </div>
            <div class="form-group">
              <label class="bold">Fecha de Nacimiento: </label>
              <input
                type="date"
                class="form-control"
                v-model="datosAutor.fecha_nac"
              />
            </div>
          </slot>
        </section>
        <footer class="modal-footer">
          <slot name="footer">
            <button
              type="button"
              class="btn btn-danger"
              @click="close"
              aria-label="Close modal"
            >
              Cerrar
            </button>
            <button type="button" class="btn btn-primary" @click="guardar">
              Guardar
            </button>
          </slot>
        </footer>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "modal",
  props: ["titulo"],
  data() {
    return {
      datosAutor: {
        nombre: "",
        dni: "",
        fecha_nac: "",
      },
    };
  },
  methods: {
    close() {
      console.log("desde hijo", this.titulo);
      this.$emit("close");
    },
    guardar() {
      this.$emit("guardar", this.datosAutor);
    },
  },
};
</script>

<style>
.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #ffffff;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
  width: 50%;
  height: 60%;
}

.modal-header,
.modal-footer {
  padding: 15px;
  display: flex;
}

.modal-header {
  border-bottom: 1px solid #eeeeee;
  color: #070707;
  justify-content: space-between;
}

.modal-footer {
  border-top: 1px solid #eeeeee;
  justify-content: flex-end;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
}

.btn-close {
  border: none;
  font-size: 20px;
  padding: 20px;
  cursor: pointer;
  font-weight: bold;
  color: #ffffff;
  background: transparent;
}

.btn-green {
  color: white;
  background: #4aae9b;
  border: 1px solid #4aae9b;
  border-radius: 2px;
}

.modal-fade-enter,
.modal-fade-leave-active {
  opacity: 0;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.5s ease;
}
</style>