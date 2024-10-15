import { Component, OnInit } from '@angular/core';
import { WebserviceService } from 'src/app/services/api/webservice.service';
import Swal from 'sweetalert2'

@Component({
  selector: 'app-cards',
  templateUrl: './cards.component.html',
  styleUrls: ['./cards.component.scss']
})
export class CardsComponent implements OnInit {

  registros: any[] = []

  constructor(private webService: WebserviceService) { }

  ngOnInit(): void {
    this.webService.getRecords().subscribe(data => {
      this.registros = data;

      console.log(this.registros)
    })
  }

  addToCart(productId: number) {
    let userId = parseInt(localStorage.getItem('userId') || '0', 10);

    this.webService.addToCart({idUsuario: userId ,idPrenda: productId}).subscribe({
      next: () => {
        
        Swal.fire({
          title: 'Producto agregado.',
          text: `El producto se ha agregado al carrito correctamente.`,
          icon: 'success',
          confirmButtonText: 'Aceptar'
        });
      },
      error: (err) => {
        console.error('Error al agregar al carrito', err);
      }
    });
  }
}
