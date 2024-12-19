import streamlit as st
import os
import subprocess

def get_available_apps():
    apps = {}
    for root, dirs, files in os.walk("apps"):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                name = f"{os.path.basename(root)}/{file[:-3]}"
                apps[name] = path
    return apps

def main():
    st.title("App Launcher")
    
    apps = get_available_apps()
    selected_app = st.selectbox("Choose an app", list(apps.keys()))
    
    if st.button("Launch"):
        subprocess.Popen(["streamlit", "run", apps[selected_app]])

if __name__ == "__main__":
    main()
