import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})

export class NavbarComponent {
  constructor(private router: Router) {}

  openRegister() {
    this.router.navigate(['/register']);
  }

  openLogin() {
    console.log("desde el login");
    
    this.router.navigate(['/login']);
  }

  goToCart() {
    this.router.navigate(['/cart']); // Asegúrate de que esta ruta esté definida en tu router
  }
}
