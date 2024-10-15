import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2'
import { AuthService } from 'src/app/services/auth/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})

export class LoginComponent {
  credentials = {
    userName: '',
    password: ''
  };

  constructor(private authService: AuthService) {}

  onSubmit() {
    this.authService.login(this.credentials).subscribe({
      next: (user) => {
        localStorage.setItem('userId', JSON.stringify(user.id));
        this.authService.redirectToHome();
      },
      error: (error) => {
        // Maneja errores, como credenciales incorrectas o problemas de red
        console.error('Error en el login', error);
        
        Swal.fire({
          title: 'Error',
          text: 'Credenciales incorrectas. Por favor, inténtalo de nuevo.',
          icon: 'error',
          confirmButtonText: 'Aceptar' // texto del botón de confirmación
        });
      }
    });
  }
}
