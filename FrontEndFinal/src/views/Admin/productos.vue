<template>
	<vx-card>
		<vs-table stripe title="Sectores" pagination max-items="7" search :data="arrayData" noDataText="No hay datos disponibles">
			<template slot="header">
			<vs-button @click="abrirForm=true" icon-pack="feather" icon="icon-plus-circle" icon-after>Nuevo</vs-button>
			</template>
				<template slot="thead">
					<vs-th >Nombre</vs-th>
					<vs-th >Descripción</vs-th>
					<vs-th >Existencia</vs-th>
					<vs-th >Precio</vs-th>
					<vs-th >Categoria</vs-th>
					<vs-th >Acciones</vs-th>
				</template>

				<template slot-scope="{data}">
					<vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

						<vs-td :data="data[indextr].nombre">
							{{data[indextr].nombre}}
						</vs-td>

						<vs-td :data="data[indextr].descripcion">
							{{data[indextr].descripcion}}
						</vs-td>

						<vs-td :data="data[indextr].existencia">
							{{data[indextr].existencia}}
						</vs-td>
						<vs-td :data="data[indextr].precio">
							{{data[indextr].precio}}
						</vs-td>

						<vs-td :data="data[indextr].categoria">
							{{data[indextr].categoria}}
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
				title="Editar Producto"
				accept-text= "Guardar"
				@accept="EditarProducto"
				:active.sync="abrirEditar"
				@cancel="close"
				@close="close"
				>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Nombre" v-model="nombreT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Descripcion" v-model="descripcionT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Existencia" v-model="existenciaT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Precio" v-model="precioT"></vs-input>
				<small>Categoria</small>
					<v-select name="Categoria" label="nombre" :options="listadoCategorias" v-model="categoria_idT" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
				<span class="text-danger">{{ errors.first('aldea') }}</span>
			</vs-prompt>
			<vs-prompt
				class="calendar-event-dialog"
				title="Guardar Producto"
				accept-text= "Guardar"
				@accept="AgregarProducto"
				:active.sync="abrirForm"
				@cancel="close"
				@close="close"
				>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Nombre" v-model="nombre"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Descripcion" v-model="descripcion"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Existencia" v-model="existencia"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Precio" v-model="precio"></vs-input>
				<small>Categoria</small>
					<v-select name="Categoria" label="nombre" :options="listadoCategorias" v-model="categoria_id" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
				<span class="text-danger">{{ errors.first('aldea') }}</span>
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
			listadoCategorias:[],
			abrirForm:false,
			abrirEditar:false,
			langHe: es,
			langEn: es,
			endDate: '',
			startDate: '',
			id: 0,
			nombre:0,
			descripcion: null,
			existencia:'',
			categoria:null,
			nombre:"",
			descripcion:"",
			existencia:"",
			precio:"",
			categoria_id:"",
			total:"",
			nombreT:"",
			descripcionT:"",
			existenciaT:"",
			precioT:"",
			categoria_idT:"",
			totalT:""
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
		Editar(datos){
			console.log(datos)
			this.nombreT=datos.nombre
			this.descripcionT=datos.descripcion
			this.existenciaT=datos.existencia
			this.precioT=datos.precio
			this.categoria_idT=datos.categoria
			this.abrirEditar=true
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
		AgregarProducto(){
			console.log('agregando producto')
		},
		EditarProducto(){
			console.log('editado aceptar')
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
				{id:1,nombre:'Primero',descripcion:'Uno',existencia:1,precio:100,categoria:'primero'},
				{id:2,nombre:'Tercero',descripcion:'Dos',existencia:1,precio:100,categoria:'primero'},
				{id:3,nombre:'Cuardo',descripcion:'Tres',existencia:1,precio:100,categoria:'primero'},
				{id:4,nombre:'Quinto',descripcion:'Cuatro',existencia:1,precio:100,categoria:'primero'}
			]
			this.listadoCategorias=[
				{id:1,nombre:'Gas'},
				{id:2,nombre:'Leche'},
				{id:3,nombre:'Comida'},
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