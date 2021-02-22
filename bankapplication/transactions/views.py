from django.shortcuts import render, redirect
from profiles.models import accountInfoModel, createProfileModel
from django.contrib import messages
# Create your views here.
from transactions.forms import TransferAmountForm, DepositAmountForm, WithdrawAmountForm, BalanceCheckForm


def transferamount(request):
    form = TransferAmountForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = TransferAmountForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            account_number = form.cleaned_data.get("account_number")
            try:
                object = accountInfoModel.objects.get(mpin=mpin)
                object1 = accountInfoModel.objects.get(account_number=account_number)
                bal = object.balance - amount
                bal1 = object1.balance + amount
                object.balance = bal
                object1.balance = bal1
                object.save()
                object1.save()

            except Exception:
                context["form"] = form
                return render(request, "transactions/transferamount.html", context)

            form.save()

            return redirect("welcomeuser")
        else:
            context["form"] = form
            return render(request, "transactions/transferamount.html", context)

    return render(request, "transactions/transferamount.html", context)


def depositamount(request):
    form = DepositAmountForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = DepositAmountForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            messages.success(request, "Deposited Successfully")
            try:
                object = accountInfoModel.objects.get(mpin=mpin)
                bal = object.balance + amount
                object.balance = bal
                object.save()


            except Exception:
                context["form"] = form
                return render(request, "transactions/depositwithdraw.html", context)

            form.save()

            return redirect("welcomeuser")
        else:
            context["form"] = form
            return render(request, "transactions/depositwithdraw.html", context)

    return render(request, "transactions/depositwithdraw.html", context)


def withdrawamount(request):
    form = WithdrawAmountForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = WithdrawAmountForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            try:
                object = accountInfoModel.objects.get(mpin=mpin)

                bal = object.balance - amount

                object.balance = bal

                object.save()


            except Exception:
                context["form"] = form
                return render(request, "transactions/depositwithdraw.html", context)

            form.save()

            return redirect("welcomeuser")
        else:
            context["form"] = form
            return render(request, "transactions/depositwithdraw.html", context)

    return render(request, "transactions/depositwithdraw.html", context)


def balance(request):
    form = BalanceCheckForm()
    context = {}
    context["form"] = form
    if (request.method == "POST"):
        form = BalanceCheckForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            try:

                object = accountInfoModel.objects.get(mpin=mpin)
                context["balance"] = object.balance
                print(object.balance)

                return render(request, "transactions/checkbalance.html", context)
            except Exception as e:
                context["form"] = form
                return render(request, "transactions/checkbalance.html", context)

    return render(request, "transactions/checkbalance.html", context)
