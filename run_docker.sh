#!/bin/bash
#parameters
container_name="gaussian"
image_name="gaussian"
image_tag="latest"

src_folder=$(pwd)/
vscodefolder=$(pwd)/vscode_container_config
data_folder=$(pwd)/data/

case $USER in
    "lorant")
        echo "Hello Lori :)"
        data_folder=/mnt/2tbSSD/data/exportready/
        ;;
    *)
        echo "Configure your data_folder path in run.sh, if needed!"
        ;;
esac


#add all the local processes to xhost, so the container reaches the window manager
xhost + local:

#if the repository is not shared promt the user to make it shared
if [[ $( git config core.sharedRepository ) != "true" ]];
then
    echo "The repository is not shared (git config core.sharedRepository)."
    echo "If you will use git at any point you should make it shared because if not the file modifications from inside the container will break git."
    echo "Would you like to make the repo shared?"
    select yn in "Yes" "No"; do
        case $yn in
            Yes )
                echo "Changing repo to shared.";
                git config core.sharedRepository true;
                break;;
            No )
                echo "Leaving it untouched.";
                break;;
        esac
    done
fi

#Set permissions for newly created files. All new files will have the following permissions.
#Important is that the group permissions of the files created are set to read and write and execute.
#We add src as a volume, so we will be able to edit and delete the files created in the container.
setfacl -PRdm u::rwx,g::rwx,o::r ./

#check if container exists
if [[ $( docker ps -a -f name=$container_name | wc -l ) -eq 2 ]];
then
    echo "Container already exists. Do you want to restart it or remove it?"
    select yn in "Restart" "Remove"; do
        case $yn in
            Restart )
                echo "Restarting it... If it was started without USB, it will be restarted without USB.";
                docker restart $container_name;
                break;;
            Remove )
                echo "Stopping it and deleting it... You should simply run this script again to start it.";
                docker stop $container_name;
                docker rm $container_name;
                break;;
        esac
    done
else
    echo "Container does not exist. Creating it."
    #NVIDIA_VISIBLE_DEVICES and NVIDIA_DRIVER_CAPABILITIES sets the visible devices and capabilities of the GPU
    #gpus all adds all the gpus to the container
    #runtime=nvidia tells the docker engine to use the nvidia runtime
    #these parameters are needed for the gpu to work properly inside the container
    docker run \
        --env DISPLAY=${DISPLAY} \
        --env NVIDIA_VISIBLE_DEVICES=all \
        --env NVIDIA_DRIVER_CAPABILITIES=all \
        --volume $data_folder:/home/appuser/gaussian/data/ \
        --volume $src_folder:/home/appuser/gaussian/main_code \
        --volume $vscodefolder:/home/appuser/gaussian/.vscode/ \
        --volume /tmp/.X11-unix:/tmp/.X11-unix \
        --network host \
        --interactive \
        --tty \
        --detach \
        --gpus all \
        --runtime=nvidia \
        --name $container_name \
        --ipc=host \
        $image_name:$image_tag 
fi
#"--ipc=host" solves error: low shm limit, solution from: https://github.com/ultralytics/yolov5/issues/4964#issuecomment-1226976208
        
