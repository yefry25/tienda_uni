import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class AuthService {
  private apiUrl = 'http://127.0.0.1:5000'; // Cambia esto por tu URL

  constructor(private http: HttpClient, private router: Router) {}

  register(userData: any) {
    return this.http.post(`${this.apiUrl}/createUser`, userData);
  }

  login(credentials: { userName: string, password: string }): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    
    // Hacemos la petición POST al servidor con las credenciales en el body
    return this.http.post(`${this.apiUrl}/login`, credentials, { headers });
  }

  redirectToHome() {
    this.router.navigate(['/']); // Cambia esto a tu ruta principal
  }
}
