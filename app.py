# importing libraries
from flask import Flask, request, jsonify, render_template, abort, redirect
from flask_mysqldb import MySQLdb
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

