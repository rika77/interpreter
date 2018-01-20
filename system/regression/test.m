# 49個を採用し、1個でcheckする

clear all
# rand : equal
rand("state", 0)
# randn : normal distribution
randn("state", 0)

n=50
N=100

# linspace(from,to,point) : from ~ to separate point
x = linspace(-3,3,n)'	# big step
X = linspace(-3,3,N)'	# small step

l_x = x(1:49)

theta = pi*x
y = sin(theta)./(theta) + 0.1*x + 0.2*randn(n,1)
l_y = y(1:49)
# plot(x,y)
x2 = x.^2

hh = 2*0.3^2
l_x2 = x2(1:49)
m = 49
sub1 = repmat(l_x2,1,m)
sub2 = repmat(l_x2',m,1)
sub3 = 2*l_x*l_x'
k = exp((-sub1 - sub2 + sub3)/hh)

# 正則化parameter lを決定
l = (k'*l_y)'
t = (k^2+diag(l))\(k*l_y) # eyeは単位行列

X2 = X.^2
K = exp((-repmat(X2,1,m) - repmat(l_x2',N,1) + 2*X*l_x')/hh)
F = K*t

# テスト誤差は?
xdash = x(50)
ydash = y(50)
fxdash = 

figure(1)
clf #グラフをclear
hold on
axis([-2.8 2.8 -1 1.5])
plot(X,F,'g-')
plot(x,y,'bo')




