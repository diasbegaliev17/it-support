import logging

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TicketForm, TicketUpdateForm
from .models import Ticket

logger = logging.getLogger(__name__)


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})


def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()  # status модельде әдепкі бойынша "new"
            logger.info("Өтінім сақталды: id=%s", ticket.pk)
            messages.success(request, "Өтінім сәтті жіберілді.")
            return redirect("ticket_list")
        # Құпия мәндер мен толық сипаттама журналға жазылмайды
        logger.warning(
            "Өтінім формасы тексеруден өтпеді: қате өрістер=%s",
            ", ".join(form.errors.keys()),
        )
    else:
        form = TicketForm()
    return render(
        request,
        "tickets/ticket_form.html",
        {"form": form, "heading": "Жаңа өтінім"},
    )


def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = TicketUpdateForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            logger.info("Өтінім жаңартылды: id=%s", ticket.pk)
            messages.success(request, "Өтінім жаңартылды.")
            return redirect("ticket_list")
        logger.warning(
            "Өтінім формасы тексеруден өтпеді: қате өрістер=%s",
            ", ".join(form.errors.keys()),
        )
    else:
        form = TicketUpdateForm(instance=ticket)
    return render(
        request,
        "tickets/ticket_form.html",
        {"form": form, "heading": "Өтінімді өңдеу"},
    )


def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        ticket_id = ticket.pk
        ticket.delete()
        logger.info("Өтінім жойылды: id=%s", ticket_id)
        messages.success(request, "Өтінім жойылды.")
        return redirect("ticket_list")
    return render(request, "tickets/ticket_confirm_delete.html", {"ticket": ticket})
