import { Component, OnInit } from '@angular/core';
import { WebserviceService } from 'src/app/services/api/webservice.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {

  cartItems: Product[] = [];

  constructor(private webService: WebserviceService) { }

  ngOnInit(): void {
    this.loadCart();
  }

  totalValue(): number {
    console.log(this.cartItems);
    

    return this.cartItems.reduce((total, item) => total + Number(item.Valor), 0);
  }
  
  loadCart() {
    let userId = parseInt(localStorage.getItem('userId') || '0', 10);

    this.webService.getOrdersByUserId(userId).subscribe(items => {
      this.cartItems = items; // Asigna los items al componente
    });
  }

  removeFromCart(productId: number) {
    /*this.cartService.removeFromCart(productId).subscribe(() => {
      this.loadCart(); // Recargar el carrito después de eliminar un item
    });*/
  }
}

export interface Product {
  IdOrden: number;
  IdUsuario: number;
  IdPrenda: number;
  Marca: string;
  Valor: number;
  Imagen: string;
  FechaCreacion: Date;
}
