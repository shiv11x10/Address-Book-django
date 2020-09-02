from django.shortcuts import render, redirect


def home(requests):
	return render(requests, 'home.html', {})


def add_address(requests):
	return render(requests, 'add_address.html', {})
