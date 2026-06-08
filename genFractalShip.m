clear;
clc;
close all;

nAttemps = 50;
pixelAverageNum = 3;

x_size = 2250;
y_size = 1500;
aspect_ratio = 3/2;

nPixels = pixelAverageNum*[x_size,y_size];

xrange = aspect_ratio * [-2.25,2.25];
yrange = [-2.25,2.25];
xVec = linspace(xrange(1),xrange(2),nPixels(1));
yVec = linspace(yrange(1),yrange(2),nPixels(2));

figure;
hold on;

button = 0;
while button ~= 120

	[X,Y] = meshgrid(xVec,yVec);
	C = X + 1i*Y;
	Z = zeros(size(C));
	nEscape = zeros(size(C));

	for ii = 1:nAttemps
		Z = (abs(real(Z)) + 1i*abs(imag(Z))).^2 + C;
		%Z = ((real(Z)) + 1i*(imag(Z))).^2 + C;
		nEscape((abs(Z) > 2) & (nEscape == 0)) = ii;
	end

	avgSide = (pixelAverageNum-1)/2;

	for ii = 1:avgSide
		nEscape = [nEscape(:,1), nEscape, nEscape(:,end)];
		nEscape = [nEscape(1,:); nEscape; nEscape(end,:)];
	end

	nEscapeCompressed = zeros(y_size,x_size);
	iiVals = 1+avgSide:pixelAverageNum:(nPixels(1)-avgSide);
	jjVals = 1+avgSide:pixelAverageNum:(nPixels(2)-avgSide);

	for kk = -avgSide:avgSide
		for mm = -avgSide:avgSide
			nEscapeCompressed = nEscapeCompressed + nEscape(jjVals+mm,iiVals+kk);
		end
	end
	nEscapeCompressed = nEscapeCompressed/(pixelAverageNum^2);

	shipColour = [0,0,0];
	glowColour = [1,1,0];
	backColour = [0.05,0.05,0.3];

	redChannel = zeros(y_size,x_size);
	greenChannel = zeros(y_size,x_size);
	blueChannel = zeros(y_size,x_size);

	redChannel(nEscapeCompressed == 0) = shipColour(1);
	greenChannel(nEscapeCompressed == 0) = shipColour(2);
	blueChannel(nEscapeCompressed == 0) = shipColour(3);

	notZero = nEscapeCompressed(nEscapeCompressed ~= 0);

	redChannel(nEscapeCompressed ~= 0) = (((notZero-1)/nAttemps)*glowColour(1) + ((nAttemps - notZero)/nAttemps)*backColour(1));
	greenChannel(nEscapeCompressed ~= 0) = (((notZero-1)/nAttemps)*glowColour(2) + ((nAttemps - notZero)/nAttemps)*backColour(2));
	blueChannel(nEscapeCompressed ~= 0) = (((notZero-1)/nAttemps)*glowColour(3) + ((nAttemps - notZero)/nAttemps)*backColour(3));

	ship = zeros(y_size,x_size,3);
	ship(:,:,1) = reshape(redChannel, [size(redChannel),1]);
	ship(:,:,2) = reshape(greenChannel, [size(greenChannel),1]);
	ship(:,:,3) = reshape(blueChannel, [size(blueChannel),1]);
	imshow(ship);
	axis equal;

	imwrite(ship,'ship.png','png');
	
	[p1,q1,button] = ginput(1);
	p1 = pixelAverageNum*round(p1);
	q1 = pixelAverageNum*round(q1);
	[p2,q2,button] = ginput(1);
	p2 = pixelAverageNum*round(p2);
	q2 = pixelAverageNum*round(q2);
	
	if button == 119
		nAttemps = 2*nAttemps;
	elseif button == 115
		nAttemps = floor(nAttemps/2);
	else
		p_low = min(p1,p2);
		p_high = max(p1,p2);
		q_low = min(q1,q2);
		q_high = max(q1,q2);
		
		x_min = xVec(p_low);
		x_max = xVec(p_high);
		
		x_centre = mean([x_min,x_max]);
		x_diff = x_max - x_min;
		
		y_min = yVec(q_low);
		y_max = yVec(q_high);
		y_diff = y_max - y_min;
		
		y_centre = mean([y_min,y_max]);
		
		ratio = (x_diff)/(y_diff);
		if ratio > (3/2)
			y_min = y_centre - (ratio/aspect_ratio)*(y_diff/2);
			y_max = y_centre + (ratio/aspect_ratio)*(y_diff/2);
		else
			x_min = x_centre - (aspect_ratio/ratio)*(x_diff/2);
			x_max = x_centre + (aspect_ratio/ratio)*(x_diff/2);
		end
		
		xrange = [x_min, x_max];
		yrange = [y_min, y_max];
		xVec = linspace(xrange(1),xrange(2),nPixels(1));
		yVec = linspace(yrange(1),yrange(2),nPixels(2));
		clf('reset');
	end
end

clear;
clc;
close all;