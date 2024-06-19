import streamlit as st
import math

st.sidebar.title(":red[HYPOTHESIS TESTING - Z TEST]")

sample_mean = st.sidebar.number_input(":green[Enter the sample mean value:]")
population_mean= st.sidebar.number_input(":green[Enter the population mean value:]")
stand_dev_population = st.sidebar.number_input(":green[Enter the standard deviation of the population:]")
sample_number= st.sidebar.number_input(":green[Enter the number of samples:]")
allowable_error = st.sidebar.number_input(":green[Enter the allowable error(0.01 or 0.05 or 0.10):]")

if st.sidebar.button(":blue[Calculate]"):
    z_test = ((sample_mean - population_mean)*math.sqrt(sample_number))/stand_dev_population
    st.write(":orange[z test value is:]",z_test)
#) conditions for the error range
    if allowable_error == 0.05:
        if z_test < 1.96 and z_test > -1.96:
            st.success("The 5% error is in acceptable range. \n****Accept the null hypothesis****\n")
        else:
            st.error("The 5% error is not in acceptable range. \n****Reject the null hypothesis****\n")
    elif allowable_error == 0.01:
        if z_test < 2.58 and z_test > -2.58:
            st.success("The 1% error is in acceptable range. \n****Accept the null hypothesis****\n")
        else:
            st.error("The 1% error is not in acceptable range. \n****Reject the null hypothesis****\n")
    elif allowable_error == 0.1:
        if z_test < 1.65 and z_test > -1.65:
            st.success("The 10% error is in acceptable range. \n****Accept the null hypothesis****\n")
        else:
            st.error("The 10% error is not in acceptable range. \n****Reject the null hypothesis****\n")
    else:
        st.error("Enter the allowable error value correctly")