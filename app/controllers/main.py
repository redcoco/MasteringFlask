# -*- coding: utf-8 -*-
"""

"""
from flask import Blueprint, redirect, url_for

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)


@main_blueprint.route('/')
def index():
    return redirect(url_for('blog.home'))