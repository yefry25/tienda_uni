import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WebserviceService {

  private apiUrl = "http://127.0.0.1:5000"
  items= [];

  constructor(private http: HttpClient) { }

  // Método para obtener los registros del web service
  getRecords(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/clothes`);
  }

  addToCart(data: {idUsuario: number, idPrenda: number}): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    
    return this.http.post(`${this.apiUrl}/createOrder`, data, { headers } ); // Envía el ID del producto
  }

  getOrdersByUserId(idUsuario: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/orderDetail/${idUsuario}`)
  }
}
