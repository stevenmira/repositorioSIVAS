from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import DeleteView, ListView, DetailView
# from django.views.generic.list import ListView,

# Create your views here.
from appAdminAplicacion.models import linea_aerea
from appAdminVuelo.forms import LineaForm


class linea_list(ListView):
    model = linea_aerea
    template_name = "lineaAerea/linea_list.html"
    paginate_by = 10


def lineaCreate(request):
    if request.method == 'POST':
        form = LineaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('aav:linea_list')
    else:
        form = LineaForm()
        return render(request, 'lineaAerea/linea_create.html', {'form': form})


def lineaUpdate(request, id_linea):
    linea = linea_aerea.objects.get(codigo_linea_aerea=id_linea)
    if request.method == 'GET':
        form = LineaForm(instance=linea)
    else:
        form = LineaForm(request.POST, instance=linea)
        if form.is_valid():
            form.save()
        return redirect('aav:linea_list')
    return render(request, 'lineaAerea/linea_create.html', {'form': form})


"""def lineaDelete(request, id_linea):
    linea = linea_aerea.objects.get(codigo_linea_aerea=id_linea)
    if request.method == 'POST':
    linea.delete()
    return redirect('aav:linea_list')
    return render(request, 'lineaAerea/linea_delete.html', {'linea': linea})
"""


class lineaDelete(DeleteView):
    model = linea_aerea
    template_name = "lineaAerea/linea_delete.html"
    success_url = reverse_lazy('aav:linea_list')


# class lineaDetail(DetailView):
#       model = linea_aerea


def lineaDetail(request, pk):
    try:
        linea_id = linea_aerea.objects.get(codigo_linea_aerea=pk)
    except linea_aerea.DoesNotExist:
        raise Http404("Linea Aerea does not exist")

    # book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'lineaAerea/linea_detail.html',
        context={'linea': linea_id, }
    )