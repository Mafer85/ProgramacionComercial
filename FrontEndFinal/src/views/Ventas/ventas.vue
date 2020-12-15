<template>
	<vx-card>
		<vs-table stripe title="Sectores" pagination max-items="7" search :data="arrayData" noDataText="No hay datos disponibles">
			<template slot="header">
			<vs-button @click="abrirForm=true" icon-pack="feather" icon="icon-plus-circle" icon-after>Nuevo</vs-button>
			</template>
				<template slot="thead">
					<vs-th >Serie</vs-th>
					<vs-th >Cliente</vs-th>
					<vs-th >NIT</vs-th>
					<vs-th >Producto</vs-th>
					<vs-th >Cantidad</vs-th>
					<vs-th >Fecha</vs-th>
					<vs-th >Total</vs-th>
					<vs-th >Acciones</vs-th>
				</template>

				<template slot-scope="{data}">
					<vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
						<vs-td :data="data[indextr].serie">
							{{data[indextr].serie}}
						</vs-td>

						<vs-td :data="data[indextr].cliente">
							{{data[indextr].cliente}}
						</vs-td>
						<vs-td :data="data[indextr].NIT">
							{{data[indextr].NIT}}
						</vs-td>
						<vs-td :data="data[indextr].productoN">
							{{data[indextr].productoN}}
						</vs-td>
						<vs-td :data="data[indextr].cantidad">
							{{data[indextr].cantidad}}
						</vs-td>
						<vs-td :data="data[indextr].fecha">
							{{data[indextr].fecha}}
						</vs-td>
						<vs-td :data="data[indextr].total">
							{{data[indextr].total}}
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
				title="Agregar Venta"
				accept-text= "Guardar"
				@accept="AgregarProducto"
				:active.sync="abrirForm"
				@cancel="close"
				@close="close"
				>
				<div class="my-4">
					<small class="date-label">Fecha de Factura</small>
			        <datepicker :language="$vs.rtl ? langHe : langEn" name="end-date" v-model="fecha"></datepicker>
				</div>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Serie" v-model="serie"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Cliente" v-model="cliente"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="NIT" v-model="NIT"></vs-input>
				<small>Producto</small>
					<v-select label="nombre" :options="listadoProductos" v-model="producto_id" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Cantidad" v-model="cantidad"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Total" v-model="total"></vs-input>
			</vs-prompt>
			<vs-prompt
				class="calendar-event-dialog"
				title="Editar Producto"
				accept-text= "Guardar"
				@accept="EditarProducto"
				:active.sync="abrirEditar"
				@cancel="close"
				@close="close"
				>
				<div class="my-4">
					<small class="date-label">Fecha de Factura</small>
			        <datepicker :language="$vs.rtl ? langHe : langEn" name="end-date" v-model="fechaT"></datepicker>
				</div>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Serie" v-model="serieT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Cliente" v-model="clienteT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="NIT" v-model="NITT"></vs-input>
				<small>Producto</small>
					<v-select label="nombre" :options="listadoProductos" v-model="producto_idT" :dir="$vs.rtl ? 'rtl' : 'ltr'" />
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Cantidad" v-model="cantidadT"></vs-input>
				<vs-input name="event-name" v-validate="'required'" class="w-full mt-8" label-placeholder="Total" v-model="totalT"></vs-input>
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
			arrayData: [],
			listadoProductos:[],
			abrirForm:false,
			abrirEditar:false,
			langHe: es,
			langEn: es,
			endDate: '',
			startDate: '',
			id: 0,
			serie: "",
			NIT:"",
			producto_id:null,
			cantidad:0,
			fecha:"",
			total:0,
			cliente:"",
			producto_idT:null,
			idT: 0,
			serieT: "",
			NITT:"",
			producto_idT:null,
			cantidadT:0,
			fechaT:"",
			totalT:0,
			clienteT:""
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
		AgregarProducto(){
			console.log('agregando producto')
		},
		EditarProducto(){
			console.log('agregando producto')
		},
		Editar(dato){
			console.log(dato)
			this.producto_idT=dato.ProductoN,
			this.idT= dato.id,
			this.serieT= dato.serie,
			this.NITT=dato.NIT,
			this.cantidadT=dato.cantidad,
			this.fechaT=new Date(dato.fecha),
			this.totalT=dato.total,
			this.clienteT=dato.cliente
			this.abrirEditar=true
		},
		Eliminar(id){
			let titulo = '';
			let color = '';

			this.$vs.dialog({
				type:'confirm',
				color: 'danger',
				title: 'Eliminar Factura',
				text: '¿Está seguro de eliminar la factura?',
				accept: this.delete,
				cancel: this.close,
				acceptText: 'Aceptar',
				cancelText: 'Cancelar',
			})
		},
		delete(){
			console.log('aceptar Eliminar')
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
				{id:1,serie:'Primero',cliente:'Uno',estado:1,NIT:"123",productoN:"asd",cantidad:5,fecha:"12-12-1998",total:150},
				{id:2,serie:'Tercero',cliente:'Dos',estado:1,NIT:"123",productoN:"asd",cantidad:5,fecha:"12-12-1998",total:150},
				{id:3,serie:'Cuardo',cliente:'Tres',estado:1,NIT:"123",productoN:"asd",cantidad:5,fecha:"12-12-1998",total:150},
				{id:4,serie:'Quinto',cliente:'Cuatro',estado:1,NIT:"123",productoN:"asd",cantidad:5,fecha:"12-12-1998",total:150}
			]
			this.listadoProductos=[
				{id:1,nombre:'Gas'},
				{id:2,nombre:'Leche'},
				{id:3,nombre:'Comida'},
			]
			this.fecha=new Date()
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

