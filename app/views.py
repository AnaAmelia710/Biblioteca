from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from django.views import View
from app.forms import LivroForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'index.html', {'livros': livros})

class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})

class EmprestimoView(View):
    def get(self, request, *args, **kwargs):
        reservas = Emprestimo.objects.all()
        return render(request, 'reserva.html', {'reservas': reservas})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})

class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})

class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Leitor.objects.all()
        return render(request, 'leitor.html', {'leitores': leitores})

class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})

#Pra deletar
class DeleteLivroView(View):
    def get(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('index')

#pra editar
class EditarLivroView(View):
    template_name = 'editar_livro.html'

    def get(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)  # Obtém o livro com o ID fornecido
        form = LivroForm(instance=livro)         # Preenche o formulário com os dados atuais do livro
        return render(request, self.template_name, {'livro': livro, 'form': form})

    def post(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)  # Obtém o livro novamente
        form = LivroForm(request.POST, instance=livro)  # Envia os dados do formulário com o livro atual

        if form.is_valid():
            form.save()  # Salva as alterações no banco
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect('editar', id=id)  # Redireciona de volta à página de edição
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'livro': livro, 'form': form})
    