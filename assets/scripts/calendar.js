import { Calendar } from '@fullcalendar/core';
import interactionPlugin from '@fullcalendar/interaction';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';

import '../styles/calendar.css'

document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');

    // Configuración del calendario
    let calendar = new Calendar(calendarEl, {
        locale: 'es',
        firstDay: 1,
        titleFormat: { year: 'numeric', month: 'long' },
        plugins: [interactionPlugin, dayGridPlugin, timeGridPlugin, listPlugin],
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
        },
        buttonText: {
            prev: 'Anterior',
            next: 'Siguiente',
            today: 'Hoy',
            dayGridMonth: 'Mes',
            timeGridWeek: 'Semana',
            timeGridDay: 'Día',
            listWeek: 'Lista'
        },
        navLinks: true,
        editable: true,
        dayMaxEvents: true,
        events: [
                { title: 'Año Nuevo', start: '2024-01-01', backgroundColor: 'lightblue', textColor: 'black' },
                { title: 'Día de Reyes', start: '2024-01-06', backgroundColor: 'lightblue', textColor: 'black' },
                { title: 'Viernes Santo', start: '2024-03-29', backgroundColor: 'lightblue', textColor: 'black' },
                { title: 'Día del Trabajo', start: '2024-05-01', backgroundColor: 'lightblue', textColor: 'black' },
                { title: 'Fiesta Nacional de España', start: '2024-10-12', backgroundColor: 'lightblue', textColor: 'black' },
                { title: 'Día de Todos los Santos', start: '2024-11-01', backgroundColor: 'lightblue', textColor: 'black' },
                { title: 'Día de la Constitución', start: '2024-12-06', backgroundColor: 'lightblue', textColor: 'black' },
                { title: 'Día de la Inmaculada Concepción', start: '2024-12-08', backgroundColor: 'lightblue', textColor: 'black' },
                { title: 'Navidad', start: '2024-12-25', backgroundColor: 'lightblue', textColor: 'black' }
        ]
    });

    // Renderizado del calendario
    calendar.render();

    // Fetch de los datos de las citas y agregado al calendario
    fetch('http://127.0.0.1:8000/obtener-citas/')
        .then(response => response.json())
        .then(data => {
            data.forEach(evento => {
                let partes = evento.fecha_cita.split('T');
                let fecha = partes[0];
                let hora = partes[1];
                calendar.addEvent({
                    title: 'Cita prof.',
                    start: fecha,
                    end: fecha,
                    backgroundColor: 'lightgreen',
                    borderColor: 'green',
                    textColor: 'black',
                    extendedProps: {
                        id: evento.id,
                        fecha_cita: evento.fecha_cita,
                        duracion: '1 hora',
                        precio: evento.precio,
                        estado: evento.estado
                    },
                });
            });
        })
        .catch(error => {
            console.error('Error al obtener los datos:', error);
        });
});
