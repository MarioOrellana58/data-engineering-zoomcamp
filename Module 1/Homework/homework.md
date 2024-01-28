## Module 1 Homework

## Docker & SQL

In this homework we'll prepare the environment 
and practice with Docker and SQL


## Question 1. Knowing docker tags

Run the command to get information on Docker 

```docker --help```

Now run the command to get help on the "docker build" command:

```docker build --help```

Do the same for "docker run".

Which tag has the following text? - *Automatically remove the container when it exits* 

- `--delete`
- `--rc`
- `--rmc`
- `--rm`

Answer: --rm 


## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use ```pip list``` ). 

What is version of the package *wheel* ?

- 0.42.0
- 1.0.0
- 23.0.1
- 58.1.0

Answer: 0.42.0 

# Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from September 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)


## Question 3. Count records 

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- 15767
- 15612
- 15859
- 89009

select count(1) from trips where lpep_pickup_datetime >= '2019-09-18' and lpep_dropoff_datetime < '2019-09-19'
Answer: 15612

## Question 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.

- 2019-09-18
- 2019-09-16
- 2019-09-26
- 2019-09-21

SELECT * FROM TRIPS
WHERE trip_distance = (
	SELECT MAX(trip_distance) FROM trips
)

Answer: 2019-09-26

## Question 5. Three biggest pick up Boroughs

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
 
- "Brooklyn" "Manhattan" "Queens"
- "Bronx" "Brooklyn" "Manhattan"
- "Bronx" "Manhattan" "Queens" 
- "Brooklyn" "Queens" "Staten Island"


SELECT DISTINCT Z."Borough"
FROM Zones Z
WHERE Z."LocationID" IN (
    SELECT T."PULocationID"
    FROM Trips T
    GROUP BY T."PULocationID"
    HAVING SUM(T.total_amount) > 50000
);

Answer: "Brooklyn" "Manhattan" "Queens"

## Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- Central Park
- Jamaica
- JFK Airport
- Long Island City/Queens Plaza

SELECT Z."Zone"
FROM Trips T
INNER JOIN Zones Z ON T."DOLocationID" = Z."LocationID"
WHERE tip_amount = (
	SELECT MAX(tip_amount)
	FROM Trips T
	INNER JOIN Zones Z ON T."PULocationID" = Z."LocationID"
	WHERE 
		lpep_pickup_datetime >= '2019-09-01' 
		AND lpep_dropoff_datetime < '2019-10-01'
		AND Z."Zone" = 'Astoria'
)

Answer: JFK Airport

## Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform. 
Copy the files from the course repo
[here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Creating Resources

After updating the main.tf and variable.tf files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.

###Check Folder 4_GCP for this


mario@LAPTOP-MHM32UUF MINGW64 /d/DOCUMENTOS/INGENIERIA/Cursos/Zoomcamp DE/DataEngineeringZoomcamp/Module 1/4_GCP (master)
$ terraform apply
google_compute_instance.de-zoomcamp: Refreshing state... [id=projects/thinking-glass-412101/zones/us-central1-a/instances/de-zoomcamp]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_compute_instance.de-zoomcamp will be created
  + resource "google_compute_instance" "de-zoomcamp" {
      + can_ip_forward       = false
      + cpu_platform         = (known after apply)
      + current_status       = (known after apply)
      + deletion_protection  = false
      + effective_labels     = {
          + "goog-ec-src" = "vm_add-tf"
        }
      + enable_display       = false
      + guest_accelerator    = (known after apply)
      + id                   = (known after apply)
      + instance_id          = (known after apply)
      + label_fingerprint    = (known after apply)
      + labels               = {
          + "goog-ec-src" = "vm_add-tf"
        }
      + machine_type         = "e2-standard-4"
      + metadata_fingerprint = (known after apply)
      + min_cpu_platform     = (known after apply)
      + name                 = "de-zoomcamp"
      + project              = "thinking-glass-412101"
      + self_link            = (known after apply)
      + tags_fingerprint     = (known after apply)
      + terraform_labels     = {
          + "goog-ec-src" = "vm_add-tf"
        }
      + zone                 = "us-central1-a"

      + boot_disk {
          + auto_delete                = true
          + device_name                = "de-zoomcamp"
          + disk_encryption_key_sha256 = (known after apply)
          + kms_key_self_link          = (known after apply)
          + mode                       = "READ_WRITE"
          + source                     = (known after apply)

          + initialize_params {
              + image                  = "projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20240110"
              + labels                 = (known after apply)
              + provisioned_iops       = (known after apply)
              + provisioned_throughput = (known after apply)
              + size                   = 30
              + type                   = "pd-balanced"
            }
        }

      + network_interface {
          + internal_ipv6_prefix_length = (known after apply)
          + ipv6_access_type            = (known after apply)
          + ipv6_address                = (known after apply)
          + name                        = (known after apply)
          + network                     = (known after apply)
          + network_ip                  = (known after apply)
          + queue_count                 = 0
          + stack_type                  = "IPV4_ONLY"
          + subnetwork                  = "projects/thinking-glass-412101/regions/us-central1/subnetworks/default"
          + subnetwork_project          = (known after apply)

          + access_config {
              + nat_ip       = (known after apply)
              + network_tier = "PREMIUM"
            }
        }

      + scheduling {
          + automatic_restart   = true
          + on_host_maintenance = "MIGRATE"
          + preemptible         = false
          + provisioning_model  = "STANDARD"
        }

      + service_account {
          + email  = "182971974119-compute@developer.gserviceaccount.com"
          + scopes = [
              + "https://www.googleapis.com/auth/devstorage.read_only",
              + "https://www.googleapis.com/auth/logging.write",
              + "https://www.googleapis.com/auth/monitoring.write",
              + "https://www.googleapis.com/auth/service.management.readonly",
              + "https://www.googleapis.com/auth/servicecontrol",
              + "https://www.googleapis.com/auth/trace.append",
            ]
        }

      + shielded_instance_config {
          + enable_integrity_monitoring = true
          + enable_secure_boot          = false
          + enable_vtpm                 = true
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_compute_instance.de-zoomcamp: Creating...
google_compute_instance.de-zoomcamp: Still creating... [10s elapsed]
google_compute_instance.de-zoomcamp: Creation complete after 13s [id=projects/thinking-glass-412101/zones/us-central1-a/instances/de-zoomcamp]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

mario@LAPTOP-MHM32UUF MINGW64 /d/DOCUMENTOS/INGENIERIA/Cursos/Zoomcamp DE/DataEngineeringZoomcamp/Module 1/4_GCP (master)
$


## Submitting the solutions

* Form for submitting: https://courses.datatalks.club/de-zoomcamp-2024/homework/hw01
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 29 January, 23:00 CET
