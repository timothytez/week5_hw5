Car(car_id, serial_number, model_number, color, year, make)

customer(customer_id, first_name, last_name, phone_number, address_id, billing_id)

staff(staff_id, first_name, last_name, address_id)

service_customer(service-customre_id, first_name, last_name, phone_number, address_id,
service-ticket, service_history, billing_id)

car_dealership(service_history, service_customer_id, customer_id, car_id, service_ticket,
address_id, billing_id, invoice)

service(service_id, service_customer-id, service_history, service_ticket, car_serial_numbre,
staff_id)

billing(biliing_id, service_id, invoice)

invoice(invoice_id, staff_id, customer_id)
kn fd