
	
		---Images limits resizer Verion 1 ---
	

Created by: 

	Niv Briman	
	april 2022


Description:

	The program takes your images and resize them (in maximum quality and proportion to the original 
	 as possible) into the desired dimensions limits and file size you desire.
	
	e.g: John wants to upload 40 photos (which some was taken via his Cannon camera)
	 to use in his website, but WorldPress limits him to 300KB and 1000X1000 px.
	 Using this program john can easily set those limits and upload the photos 
	 to WorldPress' format without having to go one-by-one each photo in Adobe's Photoshop to 
	 change the images properties by hand.


How to use:

	preperations:
	-download python3
	-download PIL moudule (python's library)
	*in future versions i'll make an auto double-click function to do those^ for ya

	use: (windows)
	-put all wanted images into the directory 'input'
	-to not get confuse with earlier runs- clear 'failed' and 'output' directories
	-double click 'run' file
	-enter image dimensions limits and file size limits when asked
	-if the program indicates very low quality-> it'll prompt and ask if you surly wants to converte it,
	   (simply type 'Y' or 'N' when asked), if you say no then the photo will be sent to 'failed' directory
	-wait until program finished
	-done! checkout 'output' directory for the results! (peek at 'failed' directory if needed)