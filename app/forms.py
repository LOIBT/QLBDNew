from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, DateField, StringField
from wtforms.validators import DataRequired

class PhanCongForm(FlaskForm):
    entrydate = DateField('Ngày', validators=[DataRequired()])
    manv = IntegerField('Mã Nhân Viên', validators=[DataRequired()])
    ca = IntegerField('Ca số', validators=[DataRequired()])
    submit = SubmitField(label='Xác Nhận')

class ChiaTuDong(FlaskForm):
    nutTuDong = SubmitField(label='TuDongPhanChia')

class TraCuuThongTinNV(FlaskForm):
    manv = IntegerField('Mã Nhân Viên', validators=[DataRequired()])
    nutTraCuuNV = SubmitField(label='TraCuuNV')

class TestForm(FlaskForm):
    makh = IntegerField(label='Ma khach hang:', validators=[DataRequired()])
    tenkh = StringField(label='Ten khach hang:', validators=[DataRequired()])
    diachi = StringField(label='Dia chi:', validators=[DataRequired()])
    sdt = StringField(label='SDT:', validators=[DataRequired()])
    LoaiKH = StringField(label='Loai Khach Hang:', validators=[DataRequired()])
    
    # stringfield
    submit = SubmitField(label='Xac nhan')

class DangKyDonForm(FlaskForm):
    makh = IntegerField(label='Ma khach hang:', default=-1)
    tenkh = StringField('Ten nguoi gui:', validators=[DataRequired()])
    sdt = StringField('So dien thoai nguoi gui:', validators=[DataRequired()])
    dc_kh = StringField('Dia khach hang:', validators=[DataRequired()])
    dc_gui = StringField('Dia chi gui:', validators=[DataRequired()])
    dc_nhan = StringField('Dia chi nhan:', validators=[DataRequired()])
    ghichu = StringField('Ghi chu:')
    mota = StringField('Mo ta:')
    dai = IntegerField(label='Chieu dai:')
    rong = IntegerField(label='Chieu rong:')
    cao = IntegerField(label='Chieu cao:')
    kl = IntegerField(label='Khoi luong:')
    ml = IntegerField(label='Ma loai:')
    cod = IntegerField(label='COD:')
    tennn = StringField('Ten nguoi nhan:', validators=[DataRequired()])
    cccd = StringField('Ten nguoi nhan:', validators=[DataRequired()])
    sdt_nn = StringField('So dien thoai nguoi nhan:', validators=[DataRequired()])
    submit = SubmitField('Xac nhan')

class SearchForm(FlaskForm):
    mavandon = StringField(label='Ma van don:', validators=[DataRequired()]) 
    submit = SubmitField('Xac nhan')

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

# users = []
# users.append(User(id=1, username='nhuvdk', password='qlbd'))
# users.append(User(id=2, username='loibt', password='qlbd'))
# users.append(User(id=3, username='linhvt', password='qlbd'))
# users.append(User(id=3, username='tienttm', password='qlbd'))