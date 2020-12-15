
<template>
	<vx-card>
		<vs-table stripe title="Sectores" pagination max-items="7" search :data="arrayData" noDataText="No hay datos disponibles">
			<template slot="header">
			<vs-button @click="abrirForm=true" icon-pack="feather" icon="icon-plus-circle" icon-after>Nuevo</vs-button>
			</template>
				<template slot="thead">
					<vs-th >ID</vs-th>
					<vs-th >Nombre</vs-th>
					<vs-th >Acciones</vs-th>
				</template>

				<template slot-scope="{data}">
					<vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

						<vs-td :data="data[indextr].nombre">
							{{data[indextr].id}}
						</vs-td>

						<vs-td :data="data[indextr].aldea_nombre">
							{{data[indextr].nombre}}
						</vs-td>
						<vs-td>
							<div class="flex items-center">
								<vx-tooltip text="Editar"><vs-button @click="Editar(data[indextr])" radius color="dark" type="flat" icon="edit" size="large">  </vs-button>  </vx-tooltip>
								<vx-tooltip text="Eliminar"><vs-button @click="Eliminar(data[indextr].id)" radius color="dark" type="flat" icon="delete" size="large"> </vs-button></vx-tooltip>
							</div>
						</vs-td>
					</vs-tr>
				</template>
			</vs-table>

			<vs-prompt
				class="calendar-event-dialog"
				title="Agregar Categoria"
				accept-text= "Guardar"
				@accept="crearCategoria"
				:active.sync="abrirForm"
				@cancel="close"
				@close="close"
				>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Nombre" v-model="nombre"></vs-input>
			</vs-prompt>

			<vs-prompt
				class="calendar-event-dialog"
				title="Editar Categoria"
				accept-text= "Guardar"
				@accept="editarCategoria"
				:active.sync="abrirEditar"
				@cancel="close"
				@close="close"
				>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Nombre" v-model="nombreT"></vs-input>
			</vs-prompt>

	</vx-card>
</template>



<script>
import VueApexCharts from 'vue-apexcharts'
import StatisticsCardLine from '@/components/statistics-cards/StatisticsCardLine.vue'
//import analyticsData from './ui-elements/card/analyticsData.js'
import ChangeTimeDurationDropdown from '@/components/ChangeTimeDurationDropdown.vue'
import VxTimeline from '@/components/timeline/VxTimeline'
// import Formulariosector from './formulariosector.vue'
import vSelect from 'vue-select'
import axios from 'axios'
import Datepicker from 'vuejs-datepicker'
import { es } from 'vuejs-datepicker/src/locale'


export default {
	data () {
		return {
			//Aqui van a guardar todas su variables.
			arrayData: [],
			abrirForm:false,
			abrirEditar:false,
			id: 0,
			nombre:'',
			nombreT:'',
		}
	},
	components: {
		VueApexCharts,
		StatisticsCardLine,
		ChangeTimeDurationDropdown,
		VxTimeline,
		Datepicker,
		vSelect,
	},
	methods: {
		traerNombre(tabla){
			tabla.forEach(function(valor, indice, array){
				valor.aldea_nombre=valor.aldea.nombre
			}); 
			return tabla
		},
		getDate(datetime) {
			let date = new Date(datetime);
			let dateString = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`;
			return dateString;
		},
		Editar(data){
			this.nombreT = data.nombre
			this.abrirEditar = true;
		},
		Eliminar(id){
			let titulo = '';
			let color = '';

			this.$vs.dialog({
				type:'confirm',
				color: 'danger',
				title: 'Eliminar Producto',
				text: '¿Está seguro de eliminar el producto?',
				accept: this.delete,
				cancel: this.close,
				acceptText: 'Aceptar',
				cancelText: 'Cancelar',
			})
		},
		delete(){
			console.log('Confirmar Eliminar')
		},
		editarCategoria(){
			console.log('editado aceptar')
		},
		crearCategoria(){
			console.log('agregando producto')
		},
		close(){
			let titulo = "Cancelado"
			let texto = "Se cancelo el ingreso"
			this.$vs.notify({
			color:'danger',
			title:`${titulo}`,
			text:`${texto}`
			})
		},
		async index(){
			let me = this;
			this.abrir_editar=false
			const response = await axios.get(`/api/sector/get?completo=true`)
			.then(function (response) {
				var respuesta= response.data;
				me.arrayData = respuesta.sectores.data;
				me.arrayData = me.traerNombre(me.arrayData)
			})
			.catch(function (error) {
				console.log(error);
			});
		},
		index2(){
			this.arrayData = [
				{id:1,nombre:'Primero',aldea_nombre:'Uno',estado:1},
				{id:2,nombre:'Tercero',aldea_nombre:'Dos',estado:1},
				{id:3,nombre:'Cuardo',aldea_nombre:'Tres',estado:1},
				{id:4,nombre:'Quinto',aldea_nombre:'Cuatro',estado:1}
			]
			this.listado_aldea=[
				{idT:1,nombre:'Gas'},
				{idT:2,nombre:'Leche'},
				{idT:3,nombre:'Comida'},
			]
		},
	},
  	mounted(){
    	//this.index();
		this.index2();
  	}
}
</script>

<style lang="scss">
#dashboard-analytics {
  .greet-user{
    position: relative;
    .decore-left{
      position: absolute;
      left:0;
      top: 0;
    }
    .decore-right{
      position: absolute;
      right:0;
      top: 0;
    }
  }
  @media(max-width: 576px) {
    .decore-left, .decore-right{
      width: 140px;
    }
  }
}
</style>
