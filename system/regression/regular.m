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

theta = pi*x
y = sin(theta)./(theta) + 0.1*x + 0.2*randn(n,1)
# plot(x,y)
x2 = x.^2

hh = 2*0.3^2

sub1 = repmat(x2,1,n)
sub2 = repmat(x2',n,1)
sub3 = 2*x*x'
k = exp((-sub1 - sub2 + sub3)/hh)

# 正則化parameter lを決定
l = (k'*y)'
t = (k^2+diag(l))\(k*y) # eyeは単位行列

X2 = X.^2
K = exp((-repmat(X2,1,n) - repmat(x2',N,1) + 2*X*x')/hh)
F = K*t

figure(1)
clf #グラフをclear
hold on
axis([-2.8 2.8 -1 1.5])
plot(X,F,'g-')
plot(x,y,'bo')




