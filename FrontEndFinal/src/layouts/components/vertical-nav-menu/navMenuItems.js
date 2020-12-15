let rolId= localStorage.getItem('Rol') ? localStorage.getItem('Rol') : null
let UsuarioN= localStorage.getItem('Usuario') ? localStorage.getItem('Usuario') : null
console.log('******************')
console.log(rolId)

export default 
	rolId=='Vendedor'?
	[
		{
			header: 'Ventas',
			icon: 'PackageIcon',
			items: [
				{
					url: '/Ventas/ventas',
					name: 'Ventas',
					slug: 'email',
					icon: 'ShoppingCartIcon',
				},
			]
		},
	]:
	[
		{
			header: 'Ventas',
			icon: 'PackageIcon',
			items: [
				{
					url: '/Ventas/ventas',
					name: 'Ventas',
					slug: 'email',
					icon: 'ShoppingCartIcon',
				},
			]
		},
		{
			header: 'Administración',
			icon: 'PackageIcon',
			items: [
			{
				url: '/admin/productos',
				name: 'Productos',
				slug: 'todo',
				icon: 'CoffeeIcon',
			},
			{
				url: '/admin/categorias',
				name: 'Categorias',
				slug: 'calendar-simple-calendar',
				icon: 'ArchiveIcon',
				tagColor: 'success',
			},
			{
				url: '/admin/empleados',
				name: 'Empleados',
				slug: 'calendar-simple-calendar',
				icon: 'UsersIcon',
				tagColor: 'success',
			},
			]
		},
	]


