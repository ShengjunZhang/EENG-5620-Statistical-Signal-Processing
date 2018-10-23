%% This is for EENG 5620 Statistical Signal Processing
%-------------------------------------------------------------------------%
% % Assignment 4 Problem 8.22 from the text book, what I am trying to do
% is to write a Monte Carlo simulation code for the problem, and then plot
% serveral pictures including the data sequences, estimator, gain, variance
% sequences.
%                                                                         %
% Copyright 2018, Shengjun(Zhang) Zhang, All rights reserved.             %
%                                                                         %
%-------------------------------------------------------------------------%
clc; clear; close all;
%-------------------------------------------------------------------------%
% % Initialize different parameters
    A = 10;
    N = 200;
    A_estimator = zeros(1, N);
    K = zeros(1, N);
    var_A = zeros(1, N);
    sigma2_0 = 1;
    x = zeros(1, N);
%-------------------------------------------------------------------------%
% % For different r 
% r = 1;
% r = 0.95;
r = 1.05;
%-------------------------------------------------------------------------%
    x0 = A + sqrt(sigma2_0)*randn;
    A_estimator(1) = x0;
    var_A(1) = sigma2_0;
    x(1) = x0;
    K(1) = 0.5; % % From (8.41)
%-------------------------------------------------------------------------%
% % Monte Carlo Simulation, generate data and update estimator, gain and variance.
for i = 2: N
        sigma2 = r^i;
        x(i) = A + sqrt(sigma2)*randn;        
        K(i) = var_A(i-1)/(var_A(i-1) + sigma2);        
        A_estimator(i) = A_estimator(i-1)+K(i)*(x(i)-A_estimator(i-1));       
        var_A(i) = (1-K(i))*var_A(i-1);
end
%-------------------------------------------------------------------------%
% % Plot
%-------------------------------------------------------------------------%
figure(1);
iteration = 1 : N;

subplot(2,2,1);
plot(iteration,  x);
xlabel('Current sample, N'),ylabel('Data');

subplot(2,2,2);
plot(iteration,  A_estimator);
xlabel('Current sample, N'),ylabel('Estimate');

subplot(2,2,3);
plot(iteration,  K);
xlabel('Current sample, N'),ylabel('Gain');

subplot(2,2,4);
plot(iteration,  var_A);
xlabel('Current sample, N'),ylabel('Variance');

suptitle('r = 1.05');
disp('Done!');
%-------------------------------------------------------------------------%
